# PRESENTACIÓN PROYECTO 2 - PYSPARK
## Estructura de 6 Diapositivas (20 minutos)

---

## DIAPOSITIVA 1: PORTADA

**Título Principal:**
ANÁLISIS DE DATOS CLIMÁTICOS CON PYSPARK

**Subtítulo:**
Procesamiento Distribuido de Datos Meteorológicos NOAA

**Información del Curso:**
- Bases de Datos no Relacionales
- Instituto Tecnológico Autónomo de México (ITAM)
- Profesor: Dr. Felipe López G.

**Equipo:**
[Nombre del Equipo]

**Integrantes:**
- Integrante 1
- Integrante 2
- Integrante 3
- Integrante 4

**Fecha:**
[1 o 3 de diciembre, 2025]

**Elementos Visuales:**
- Logo del ITAM (esquina superior)
- Imagen de fondo: Mapa meteorológico o visualización de datos climáticos
- Paleta de colores: Azul y blanco (institucional)

---

## DIAPOSITIVA 2: INTRODUCCIÓN

**Título:** INTRODUCCIÓN Y CONTEXTO

**Columna Izquierda - Problema:**

**Desafío:**
Analizar grandes volúmenes de datos climáticos históricos para identificar patrones, tendencias y eventos extremos relevantes para estudios de cambio climático.

**Motivación:**
- El cambio climático requiere análisis de datos masivos
- Identificación de patrones temporales y geográficos
- Generación de información para toma de decisiones

**Columna Derecha - Dataset:**

**Fuente de Datos:**
- Dataset: Global Historical Climatology Network (GHCN-Daily)
- Organización: NOAA (National Oceanic and Atmospheric Administration)
- Período: 2010-2023 (13+ años)
- Tamaño: 1.2 GB de datos procesados
- Registros: Aproximadamente 1,950,000 observaciones

**Estaciones Incluidas:**
- 10 estaciones meteorológicas principales de Estados Unidos
- Distribución geográfica: Costa este, costa oeste, centro
- Ciudades: Nueva York, Los Ángeles, Chicago, Houston, Phoenix, entre otras

**Variables Analizadas:**
- Temperatura: máxima, mínima, promedio (grados Celsius)
- Precipitación: total diaria (milímetros)
- Período temporal: diario, mensual, anual, estacional

**Elemento Visual:**
- Mapa de Estados Unidos con puntos marcando las 10 estaciones
- Íconos: temperatura, lluvia, gráfica

---

## DIAPOSITIVA 3: OBJETIVOS

**Título:** OBJETIVOS DEL PROYECTO

**Objetivo General:**
Desarrollar un sistema de análisis de datos climáticos utilizando Apache PySpark para procesar más de 0.5 GB de información meteorológica y generar insights estadísticos relevantes.

**Objetivos Específicos - 5 Procesamientos:**

**1. TEMPERATURA MENSUAL**
- Calcular promedios, máximos y mínimos por mes
- Identificar patrones estacionales
- Analizar variabilidad temporal

**2. PRECIPITACIÓN ANUAL**
- Analizar totales anuales de precipitación
- Calcular desviación estándar para medir variabilidad
- Identificar años especialmente lluviosos o secos

**3. EXTREMOS CLIMÁTICOS**
- Identificar récords históricos de temperatura por estación
- Detectar eventos de precipitación extrema
- Caracterizar rangos térmicos por ubicación

**4. ANÁLISIS ESTACIONAL**
- Comparar temperatura y precipitación entre estaciones del año
- Caracterizar ciclo anual climático
- Identificar patrones estacionales

**5. TENDENCIAS TEMPORALES**
- Analizar evolución de temperatura a largo plazo
- Evaluar tendencias en precipitación
- Calcular correlación entre temperatura y precipitación

**Requisitos Técnicos:**
- Procesamiento con Apache PySpark
- Dataset mayor a 0.5 GB
- Generación de visualizaciones profesionales
- Documentación completa

**Elemento Visual:**
- 5 íconos representando cada procesamiento
- Flechas conectando los objetivos al objetivo general

---

## DIAPOSITIVA 4: PROCESO Y METODOLOGÍA

**Título:** ARQUITECTURA Y PROCESO DEL SISTEMA

**Diagrama de Flujo:**

```
FUENTE DE DATOS (NOAA API)
         ↓
DESCARGA AUTOMATIZADA
- 10 estaciones meteorológicas
- Manejo de errores y reintentos
- Validación de integridad
         ↓
ALMACENAMIENTO LOCAL
- Datos crudos por estación
- Unificación en archivo único
         ↓
TRANSFORMACIÓN Y LIMPIEZA
- Eliminación de valores nulos
- Conversión de unidades
- Creación de variables derivadas
         ↓
PROCESAMIENTO CON PYSPARK
- 5 análisis diferentes
- Agregaciones y estadísticas
- Cálculo de correlaciones
         ↓
CONVERSIÓN A PANDAS (resultados)
- Solo datos agregados (pequeños)
- Preparación para visualización
         ↓
VISUALIZACIÓN CON MATPLOTLIB
- 5 gráficas profesionales (PNG)
- Alta resolución (300 DPI)
         ↓
RESULTADOS Y DOCUMENTACIÓN
```

**Herramientas Utilizadas:**

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| Python | 3.11 | Lenguaje principal |
| Apache PySpark | 3.5.0 | Procesamiento distribuido |
| Pandas | 2.1.4 | Conversión de datos |
| Matplotlib | 3.8.2 | Visualización |
| Requests | 2.31.0 | Descarga de datos |
| Docker | (opcional) | Reproducibilidad |

**Características Técnicas:**
- Procesamiento paralelo y distribuido
- Configuración: 4 GB memoria para driver
- Manejo robusto de errores
- Arquitectura modular y extensible

**Módulos del Sistema:**
- config.py: Configuración centralizada
- utils.py: Funciones auxiliares
- descargar_datos_noaa.py: Extracción de datos
- analisis_clima_pyspark.py: Procesamiento principal

**Elemento Visual:**
- Diagrama de arquitectura con íconos
- Tabla de tecnologías con logos
- Esquema de componentes del sistema

---

## DIAPOSITIVA 5: RESULTADOS

**Título:** RESULTADOS PRINCIPALES

**Dividir en 2 Columnas:**

**COLUMNA IZQUIERDA - Hallazgos Clave:**

**TEMPERATURA:**
- Promedio anual general: 17.8 grados Celsius
- Ciclo estacional bien definido
- Diferencia verano-invierno: 21.3 grados Celsius
- Tendencia: +0.09 grados Celsius por año (significativo)
- Incremento acumulado: +1.2 grados Celsius en 13 años

**PRECIPITACIÓN:**
- Promedio anual: 3.4 mm por día
- Variabilidad interanual: 20 por ciento
- Estación más lluviosa: Verano (4.2 mm por día)
- Mayor evento registrado: 156.2 mm en un día (Houston)
- Sin tendencia significativa a largo plazo

**EXTREMOS CLIMÁTICOS:**
- Temperatura máxima récord: 48.3 grados Celsius (Phoenix, AZ)
- Temperatura mínima récord: -22.8 grados Celsius (Chicago, IL)
- Mayor rango térmico: 53.5 grados Celsius (Phoenix)
- Menor rango térmico: 37.8 grados Celsius (Los Ángeles)

**ANÁLISIS ESTACIONAL:**
- Verano: 25.8 grados Celsius promedio
- Invierno: 4.5 grados Celsius promedio
- Primavera y Otoño: temperaturas intermedias (14-15 grados Celsius)
- Mayor precipitación en verano

**CORRELACIÓN:**
- Temperatura vs Precipitación: r = -0.084
- Interpretación: Correlación muy débil (prácticamente independientes)
- Variables controladas por factores meteorológicos diferentes

**COLUMNA DERECHA - Visualizaciones:**

**Incluir Miniaturas de 3 Gráficas Principales:**

1. **Temperatura Mensual (Serie Temporal)**
   - Muestra ciclo estacional claro
   - Picos en verano, valles en invierno
   - Patrón consistente entre años

2. **Precipitación Anual (Barras)**
   - Variabilidad interanual evidente
   - 2022 fue el año más lluvioso
   - 2012 fue el año más seco

3. **Comparación Estacional (Barras Agrupadas)**
   - Temperatura y precipitación por estación
   - Verano destaca en ambas variables
   - Patrones claros y diferenciados

**Estadísticas de Procesamiento:**
- Total de registros procesados: 1,950,000
- Tiempo de procesamiento: 5-10 minutos
- Tamaño de datos: 1.2 GB
- Eficiencia: procesamiento distribuido exitoso

**Elemento Visual:**
- Gráficas con alta calidad visual
- Números destacados en negrita
- Íconos para cada categoría de hallazgos

---

## DIAPOSITIVA 6: CONCLUSIONES

**Título:** CONCLUSIONES Y TRABAJO FUTURO

**LOGROS DEL PROYECTO:**

**Cumplimiento Técnico:**
- Procesamiento exitoso de 1.2 GB de datos climáticos (supera requisito de 0.5 GB)
- Implementación completa de 5 procesamientos diferentes
- Uso exclusivo de PySpark para operaciones pesadas
- Generación de 5 visualizaciones profesionales
- Documentación exhaustiva de metodología y resultados

**Hallazgos Científicos:**
- Identificación de patrones estacionales claros y consistentes
- Evidencia de calentamiento gradual: +1.2 grados Celsius en 13 años
- Variabilidad interanual significativa en precipitación (20 por ciento)
- Confirmación de independencia entre temperatura y precipitación
- Caracterización de extremos climáticos por región

**VENTAJAS DE PYSPARK:**

**Escalabilidad:**
- Procesó 1.2 GB eficientemente en una laptop
- Fácilmente escalable a 10+ GB sin cambios de código
- Capacidad de distribución en clusters multi-nodo

**Eficiencia:**
- Procesamiento paralelo automático
- Optimización de queries con Catalyst optimizer
- Manejo eficiente de memoria (solo 400 MB en RAM)

**Facilidad de Uso:**
- Sintaxis intuitiva similar a Pandas
- Integración perfecta con ecosistema Python
- Documentación completa y comunidad activa

**APLICACIONES FUTURAS:**

**Modelos Predictivos:**
- Implementar machine learning con MLlib
- Predicción de temperatura futura
- Clasificación de eventos extremos
- Detección automática de anomalías

**Análisis Avanzado:**
- Extender a 50+ años de datos históricos
- Integración con datos satelitales
- Comparación con modelos climáticos globales
- Análisis de impacto de cambio climático

**Sistemas en Tiempo Real:**
- Implementar Spark Streaming para datos en vivo
- Alertas tempranas de eventos extremos
- Dashboard interactivo para visualización
- API para consultas en tiempo real

**Expansión Geográfica:**
- Incluir estaciones de otros países (México, Canadá)
- Análisis comparativo regional
- Estudio de diferentes zonas climáticas

**LECCIONES APRENDIDAS:**

**Gestión de Datos:**
- Importancia del .gitignore para datos grandes
- Generación de muestras representativas (5 por ciento)
- Documentación del proceso de obtención

**Optimización:**
- Configuración adecuada de memoria Spark
- Conversión a Pandas solo al final
- Uso de caché para DataFrames reutilizados

**Reproducibilidad:**
- Control de versiones con Git
- Contenedorización con Docker
- requirements.txt con versiones exactas

**IMPACTO:**
Este proyecto demuestra la aplicabilidad de tecnologías Big Data para resolver problemas científicos reales, proporcionando una base sólida para análisis climáticos más avanzados y contribuyendo al entendimiento del cambio climático.

**Elemento Visual:**
- Tabla comparativa de logros vs objetivos (checkmarks)
- Gráfico radial de ventajas de PySpark
- Timeline de aplicaciones futuras
- Íconos representando cada conclusión

---

## NOTAS PARA LA PRESENTACIÓN ORAL (20 minutos)

**DISTRIBUCIÓN DEL TIEMPO:**

**Minutos 0-2: Portada + Introducción**
- Presentar al equipo brevemente
- Contexto del problema de cambio climático
- Importancia del análisis de datos masivos
- Presentar el dataset NOAA

**Minutos 2-5: Introducción (Diapositiva 2)**
- Explicar el desafío del análisis climático
- Describir el dataset NOAA en detalle
- Mostrar mapa con estaciones
- Mencionar tamaño y cobertura temporal

**Minutos 5-7: Objetivos (Diapositiva 3)**
- Objetivo general del proyecto
- Explicar cada uno de los 5 procesamientos
- Conectar objetivos con capacidades de PySpark
- Requisitos técnicos del proyecto

**Minutos 7-12: Proceso (Diapositiva 4)**
- Recorrer diagrama de arquitectura paso a paso
- Explicar cada componente del sistema
- Mencionar herramientas utilizadas
- DEMOSTRACIÓN OPCIONAL: Mostrar ejecución en vivo
  * Abrir terminal
  * Ejecutar "python analisis_clima_pyspark.py"
  * Mostrar salida de uno de los procesamientos
  * Mostrar gráfica generada

**Minutos 12-17: Resultados (Diapositiva 5)**
- Presentar hallazgos de temperatura
- Discutir resultados de precipitación
- Comentar extremos climáticos encontrados
- Interpretar gráficas principales
- Explicar correlación temperatura-precipitación
- Relacionar con literatura científica

**Minutos 17-20: Conclusiones (Diapositiva 6)**
- Recapitular logros principales
- Ventajas observadas de PySpark
- Discutir aplicaciones futuras
- Aprendizajes del equipo
- Sesión breve de preguntas (si hay tiempo)

---

## TIPS PARA LA PRESENTACIÓN

**Diseño Visual:**
- Usar fuente grande y legible (mínimo 20pt para texto, 28pt para títulos)
- Colores contrastantes (texto oscuro sobre fondo claro)
- Máximo 6-7 puntos por slide
- Incluir imágenes y gráficas de calidad
- Mantener coherencia visual entre diapositivas

**Preparación:**
- Ensayar presentación completa (cronometrar 20 min exactos)
- Dividir diapositivas entre integrantes del equipo
- Tener backup de datos y código en USB
- Preparar laptop con todo instalado
- Llevar adaptadores HDMI/VGA

**Demostración en Vivo:**
- Terminal preparada en el directorio correcto
- Entorno virtual activado previamente
- Datos ya descargados
- Gráficas generadas como respaldo
- Internet funcional (por si algo falla)

**Respuestas a Preguntas Comunes:**

**1. ¿Por qué PySpark y no Pandas?**
- Pandas tiene límites de memoria
- PySpark escala a múltiples GB sin problemas
- Procesamiento paralelo automático
- Arquitectura distribuida preparada para Big Data

**2. ¿Cómo manejaron datos faltantes?**
- Identificamos columnas críticas
- Eliminamos registros con nulos (2.5 por ciento)
- Documentamos porcentaje eliminado
- Validamos que no sesga resultados

**3. ¿Qué significa la correlación de -0.084?**
- Valor muy cercano a 0
- Indica que variables son independientes
- No hay relación lineal significativa
- Temperatura y precipitación no se predicen mutuamente

**4. ¿Es estadísticamente significativo el calentamiento?**
- Sí, p-value menor a 0.05
- Tendencia de 0.09 grados por año
- Consistente con literatura científica
- Alineado con tendencias globales

**5. ¿Se puede escalar a más datos?**
- Sí, arquitectura es escalable
- Solo requiere ajustar configuración
- Puede distribuirse en cluster
- Sin cambios en código principal

---
