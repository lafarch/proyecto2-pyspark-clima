"""
Script para descargar datos climáticos de NOAA
Dataset: Global Historical Climatology Network (GHCN-Daily)
"""

import requests
import os
import pandas as pd
from pathlib import Path
from config import (
    DATOS_DIR, 
    ESTACIONES_NOAA, 
    NOAA_BASE_URL,
    DATOS_CRUDOS,
    DATOS_PROCESADOS,
    REQUISITOS
)
from utils import (
    imprimir_banner,
    verificar_tamaño_archivo,
    listar_archivos_datos
)


def descargar_estacion(estacion, output_dir):
    """
    Descarga datos de una estación específica
    
    Args:
        estacion: Código de estación NOAA
        output_dir: Directorio de salida
        
    Returns:
        str: Path del archivo descargado o None si falló
    """
    try:
        url = f"{NOAA_BASE_URL}{estacion}.csv"
        filename = output_dir / f"{estacion}.csv"
        
        print(f"Descargando {estacion}...", end=" ", flush=True)
        
        response = requests.get(url, stream=True, timeout=60)
        
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            tamaño_mb = os.path.getsize(filename) / (1024 * 1024)
            print(f"OK ({tamaño_mb:.1f} MB)")
            return filename
        else:
            print(f"ERROR {response.status_code}")
            return None
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None


def descargar_todas_estaciones():
    """
    Descarga datos de todas las estaciones configuradas
    
    Returns:
        list: Lista de archivos descargados
    """
    imprimir_banner("DESCARGA DE DATOS NOAA")
    
    # Crear directorio para datos crudos
    datos_noaa_dir = DATOS_DIR / "datos_noaa"
    datos_noaa_dir.mkdir(exist_ok=True)
    
    print(f"\nDescargando {len(ESTACIONES_NOAA)} estaciones meteorológicas")
    print(f"Destino: {datos_noaa_dir}\n")
    
    archivos_descargados = []
    
    for idx, estacion in enumerate(ESTACIONES_NOAA, 1):
        print(f"[{idx:2d}/{len(ESTACIONES_NOAA)}] ", end="")
        archivo = descargar_estacion(estacion, datos_noaa_dir)
        
        if archivo:
            archivos_descargados.append(archivo)
    
    # Resumen
    imprimir_banner("RESUMEN DE DESCARGA")
    print(f"\nArchivos descargados: {len(archivos_descargados)}/{len(ESTACIONES_NOAA)}")
    
    tamaño_total_gb = sum(os.path.getsize(f) for f in archivos_descargados) / (1024**3)
    print(f"Tamaño total: {tamaño_total_gb:.2f} GB")
    
    if tamaño_total_gb >= REQUISITOS['tamaño_minimo_gb']:
        print(f"Cumple requisito mínimo (>{REQUISITOS['tamaño_minimo_gb']} GB)")
    else:
        print(f"Advertencia: Tamaño menor a {REQUISITOS['tamaño_minimo_gb']} GB")
        print("   Considera descargar más estaciones")
    
    return archivos_descargados


def unificar_archivos(archivos):
    """
    Unifica múltiples archivos CSV en uno solo
    
    Args:
        archivos: Lista de paths a archivos CSV
        
    Returns:
        str: Path del archivo unificado
    """
    if not archivos:
        print("No hay archivos para unificar")
        return None
    
    imprimir_banner("UNIFICACIÓN DE ARCHIVOS")
    
    print(f"\nUnificando {len(archivos)} archivos...")
    
    dfs = []
    for archivo in archivos:
        try:
            # Leer solo columnas necesarias para ahorrar memoria
            columnas = ['STATION', 'DATE', 'TMAX', 'TMIN', 'PRCP']
            df = pd.read_csv(archivo, usecols=lambda x: x in columnas)
            dfs.append(df)
            print(f"   OK {Path(archivo).name}: {len(df):,} registros")
        except Exception as e:
            print(f"   ERROR en {Path(archivo).name}: {e}")
    
    if not dfs:
        print("No se pudo leer ningún archivo")
        return None
    
    # Combinar todos los DataFrames
    print("\nCombinando datos...")
    df_unificado = pd.concat(dfs, ignore_index=True)
    
    # Guardar archivo unificado
    print(f"Guardando archivo unificado...")
    df_unificado.to_csv(DATOS_CRUDOS, index=False)
    
    print(f"\nArchivo unificado creado: {DATOS_CRUDOS.name}")
    print(f"   Registros totales: {len(df_unificado):,}")
    print(f"   Periodo: {df_unificado['DATE'].min()} a {df_unificado['DATE'].max()}")
    print(f"   Columnas: {list(df_unificado.columns)}")
    
    # Verificar tamaño
    verificar_tamaño_archivo(DATOS_CRUDOS, REQUISITOS['tamaño_minimo_gb'])
    
    return DATOS_CRUDOS


def preparar_datos_para_pyspark(archivo):
    """
    Limpia y prepara datos para PySpark
    
    Args:
        archivo: Path del archivo a procesar
        
    Returns:
        str: Path del archivo procesado
    """
    if not archivo or not os.path.exists(archivo):
        print(f"Archivo no encontrado: {archivo}")
        return None
    
    imprimir_banner("PREPARACIÓN PARA PYSPARK")
    
    print("\nLeyendo datos...")
    df = pd.read_csv(archivo)
    
    print(f"   Registros iniciales: {len(df):,}")
    
    # Limpieza de datos
    print("\nLimpiando datos...")
    
    # 1. Eliminar filas con valores nulos en columnas críticas
    antes = len(df)
    df = df.dropna(subset=['TMAX', 'TMIN', 'PRCP'])
    print(f"   Eliminadas {antes - len(df):,} filas con valores nulos")
    
    # 2. Convertir fechas y extraer componentes
    print("   Procesando fechas...")
    df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
    
    # Eliminar filas con fechas inválidas
    antes_fecha = len(df)
    df = df.dropna(subset=['DATE'])
    if antes_fecha > len(df):
        print(f"   Eliminadas {antes_fecha - len(df):,} filas con fechas inválidas")
    
    df['YEAR'] = df['DATE'].dt.year
    df['MONTH'] = df['DATE'].dt.month
    df['DAY'] = df['DATE'].dt.day
    
    # 3. Calcular temperatura promedio
    df['TEMP'] = (df['TMAX'] + df['TMIN']) / 2
    
    # 4. Convertir temperaturas a Celsius (NOAA usa décimas de Celsius)
    df['TMAX'] = df['TMAX'] / 10
    df['TMIN'] = df['TMIN'] / 10
    df['TEMP'] = df['TEMP'] / 10
    
    # 5. Convertir precipitación a mm (NOAA usa décimas de mm)
    df['PRCP'] = df['PRCP'] / 10
    
    # Información del dataset procesado
    print(f"\nDataset procesado:")
    print(f"   - Registros: {len(df):,}")
    print(f"   - Periodo: {df['YEAR'].min()} - {df['YEAR'].max()} ({df['YEAR'].max() - df['YEAR'].min() + 1} años)")
    print(f"   - Estaciones: {df['STATION'].nunique()}")
    print(f"   - Columnas: {list(df.columns)}")
    
    # Estadísticas rápidas
    print(f"\nEstadísticas:")
    print(f"   - Temperatura promedio: {df['TEMP'].mean():.1f} C")
    print(f"   - Temp. máxima record: {df['TMAX'].max():.1f} C")
    print(f"   - Temp. mínima record: {df['TMIN'].min():.1f} C")
    print(f"   - Precipitación promedio: {df['PRCP'].mean():.2f} mm/día")
    
    # Guardar archivo procesado
    print(f"\nGuardando datos procesados...")
    df.to_csv(DATOS_PROCESADOS, index=False)
    
    print(f"\nDatos listos para PySpark: {DATOS_PROCESADOS.name}")
    
    return DATOS_PROCESADOS


def main():
    """Función principal"""
    print("\n" + "=" * 60)
    print("PROYECTO 2 - DESCARGA Y PREPARACIÓN DE DATOS NOAA".center(60))
    print("=" * 60 + "\n")
    
    try:
        # Paso 1: Descargar datos
        print("PASO 1/3: Descarga de datos")
        archivos = descargar_todas_estaciones()
        
        if not archivos:
            print("\nNo se descargaron archivos. Verifica tu conexión a internet.")
            return
        
        # Paso 2: Unificar archivos
        print("\n" + "-" * 60)
        print("PASO 2/3: Unificación de archivos")
        archivo_unificado = unificar_archivos(archivos)
        
        if not archivo_unificado:
            print("\nError al unificar archivos")
            return
        
        # Paso 3: Preparar para PySpark
        print("\n" + "-" * 60)
        print("PASO 3/3: Preparación para PySpark")
        archivo_final = preparar_datos_para_pyspark(archivo_unificado)
        
        if not archivo_final:
            print("\nError al preparar datos")
            return
        
        # Resumen final
        imprimir_banner("PROCESO COMPLETADO")
        print(f"\nArchivos generados:")
        print(f"   1. Datos crudos: {DATOS_CRUDOS}")
        print(f"   2. Datos procesados: {DATOS_PROCESADOS}")
        
        print(f"\nPróximos pasos:")
        print(f"   1. Ejecutar: python analisis_clima_pyspark.py")
        print(f"   2. Revisar gráficas generadas en: resultados/")
        print(f"   3. Generar muestra 5% con: utils.generar_muestra()")
        
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()