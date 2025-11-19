# Guía de Instalación Detallada

Esta guía proporciona instrucciones paso a paso para configurar el entorno de desarrollo del Proyecto 2: Análisis Climático con PySpark.

## Tabla de Contenidos

1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación de Python](#instalación-de-python)
3. [Instalación de Java](#instalación-de-java)
4. [Configuración del Proyecto](#configuración-del-proyecto)
5. [Instalación con Docker](#instalación-con-docker)
6. [Verificación de la Instalación](#verificación-de-la-instalación)
7. [Solución de Problemas](#solución-de-problemas)

---

## Requisitos del Sistema

### Hardware Mínimo

- **Procesador**: Dual-core 2.0 GHz o superior
- **Memoria RAM**: 4 GB (8 GB recomendado)
- **Espacio en disco**: 5 GB libres
- **Conexión a internet**: Requerida para descargar datos

### Software Base

- **Sistema Operativo**: Windows 10/11, macOS 10.15+, o Linux (Ubuntu 20.04+)
- **Python**: 3.8, 3.9, 3.10, o 3.11
- **Java**: JDK 8 u 11 (requerido por Apache Spark)
- **Git**: Para clonar el repositorio

---

## Instalación de Python

### Windows

**Opción 1: Desde python.org**

1. Descargar el instalador desde https://www.python.org/downloads/
2. Ejecutar el instalador
3. **IMPORTANTE**: Marcar la opción "Add Python to PATH"
4. Click en "Install Now"
5. Verificar instalación:

```powershell
python --version
```

**Opción 2: Usando Chocolatey**

```powershell
# Abrir PowerShell como Administrador
choco install python311
```

### macOS

**Opción 1: Usando Homebrew**

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python
brew install python@3.11
```

**Opción 2: Desde python.org**

1. Descargar el instalador desde https://www.python.org/downloads/macos/
2. Abrir el archivo .pkg y seguir instrucciones

### Linux (Ubuntu/Debian)

```bash
# Actualizar repositorios
sudo apt update

# Instalar Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip

# Verificar instalación
python3.11 --version
```

---

## Instalación de Java

Apache Spark requiere Java 8 u 11 para funcionar correctamente.

### Windows

**Opción 1: Usando Chocolatey**

```powershell
# Abrir PowerShell como Administrador
choco install openjdk11
```

**Opción 2: Manual**

1. Descargar OpenJDK desde https://adoptium.net/
2. Ejecutar el instalador
3. Configurar JAVA_HOME:
   - Abrir "Variables de entorno"
   - Agregar nueva variable del sistema:
     - Nombre: `JAVA_HOME`
     - Valor: `C:\Program Files\Eclipse Adoptium\jdk-11.x.x.x-hotspot`
   - Agregar a PATH: `%JAVA_HOME%\bin`

4. Verificar instalación:

```powershell
java -version
```

### macOS

```bash
# Instalar OpenJDK 11
brew install openjdk@11

# Configurar JAVA_HOME
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 11)' >> ~/.zshrc
source ~/.zshrc

# Verificar instalación
java -version
```

### Linux (Ubuntu/Debian)

```bash
# Instalar OpenJDK 11
sudo apt update
sudo apt install openjdk-11-jdk

# Configurar JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> ~/.bashrc
source ~/.bashrc

# Verificar instalación
java -version
```

---

## Configuración del Proyecto

### Paso 1: Clonar el Repositorio

```bash
# Clonar desde GitHub
git clone https://github.com/TU_USUARIO/proyecto2-pyspark-clima.git

# Entrar al directorio
cd proyecto2-pyspark-clima
```

### Paso 2: Crear Entorno Virtual

**Windows (PowerShell)**

```powershell
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\Activate.ps1

# Si hay error de permisos, ejecutar como Administrador:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (CMD)**

```cmd
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.venv\Scripts\activate.bat
```

**macOS/Linux**

```bash
# Crear entorno virtual
python3 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate
```

**Verificar que el entorno está activo**: Deberías ver `(.venv)` al inicio de tu línea de comando.

### Paso 3: Instalar Dependencias

```bash
# Actualizar pip
pip install --upgrade pip

# Instalar todas las dependencias
pip install -r requirements.txt

# Esto instalará:
# - pyspark==3.5.0
# - pandas==2.1.4
# - numpy==1.26.2
# - matplotlib==3.8.2
# - requests==2.31.0
# - jupyter (opcional)
```

### Paso 4: Verificar Estructura de Directorios

```bash
# Crear directorios si no existen
mkdir -p datos resultados docs

# Verificar estructura
ls -la
```

Deberías ver:

```
.venv/
datos/
resultados/
docs/
config.py
utils.py
descargar_datos_noaa.py
analisis_clima_pyspark.py
requirements.txt
...
```

---

## Instalación con Docker

Si prefieres usar Docker para evitar problemas de configuración:

### Paso 1: Instalar Docker

**Windows/Mac**

1. Descargar Docker Desktop desde https://www.docker.com/products/docker-desktop
2. Ejecutar el instalador
3. Reiniciar el sistema
4. Abrir Docker Desktop

**Linux**

```bash
# Instalar Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Instalar Docker Compose
sudo apt install docker-compose

# Agregar usuario al grupo docker
sudo usermod -aG docker $USER

# Reiniciar sesión o ejecutar:
newgrp docker
```

### Paso 2: Construir Imagen

```bash
# En el directorio del proyecto
docker-compose build
```

### Paso 3: Verificar Docker

```bash
# Probar que funciona
docker-compose run pyspark-app python utils.py
```

---

## Verificación de la Instalación

### Verificación Rápida

```bash
# Activar entorno virtual si no está activo
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Ejecutar script de verificación
python utils.py
```

Deberías ver:

```
Verificando dependencias...
   ✓ pyspark
   ✓ pandas
   ✓ matplotlib
   ✓ requests

✓ Todas las dependencias están instaladas
✓ Módulo utils.py funcionando correctamente
```

### Verificación de PySpark

```bash
python -c "import pyspark; print('PySpark version:', pyspark.__version__)"
```

Salida esperada:

```
PySpark version: 3.5.0
```

### Verificación de Java

```bash
java -version
```

Salida esperada (puede variar):

```
openjdk version "11.0.x" 2024-xx-xx
OpenJDK Runtime Environment (build 11.0.x+x)
OpenJDK 64-Bit Server VM (build 11.0.x+x, mixed mode)
```

### Prueba de Spark Session

```bash
python -c "from pyspark.sql import SparkSession; spark = SparkSession.builder.appName('Test').getOrCreate(); print('Spark funciona correctamente'); spark.stop()"
```

Si no hay errores, Spark está configurado correctamente.

---

## Solución de Problemas

### Problema 1: "python: command not found"

**Solución Windows**:

```powershell
# Verificar PATH
$env:PATH

# Agregar Python al PATH manualmente
# Panel de Control > Sistema > Variables de entorno
# Agregar: C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python311
```

**Solución Mac/Linux**:

```bash
# Usar python3 en lugar de python
python3 --version

# O crear alias
echo 'alias python=python3' >> ~/.bashrc
source ~/.bashrc
```

### Problema 2: "Java not found"

**Verificar JAVA_HOME**:

```bash
# Windows
echo %JAVA_HOME%

# Mac/Linux
echo $JAVA_HOME
```

Si está vacío, configurar según las instrucciones de instalación de Java arriba.

### Problema 3: Error al activar entorno virtual en Windows

```
.venv\Scripts\Activate.ps1 : File cannot be loaded because running scripts is disabled on this system.
```

**Solución**:

```powershell
# Ejecutar PowerShell como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Intentar activar de nuevo
.venv\Scripts\Activate.ps1
```

### Problema 4: "pip: command not found"

**Solución**:

```bash
# Usar python -m pip en lugar de pip
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Problema 5: Error de permisos al instalar paquetes

**No usar sudo con pip**. En su lugar:

```bash
# Asegurarse de estar en el entorno virtual
source .venv/bin/activate

# O instalar para el usuario
pip install --user -r requirements.txt
```

### Problema 6: "Cannot connect to Docker daemon"

**Linux**:

```bash
# Iniciar Docker
sudo systemctl start docker

# Verificar estado
sudo systemctl status docker
```

**Windows/Mac**:

- Abrir Docker Desktop
- Esperar a que el ícono de Docker en la barra de tareas esté en verde

### Problema 7: Instalación lenta de paquetes

**Solución**: Usar espejo más rápido

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Problema 8: Conflictos de versiones

**Solución**: Crear entorno virtual limpio

```bash
# Eliminar entorno virtual existente
rm -rf .venv  # Mac/Linux
rmdir /s .venv  # Windows

# Crear nuevo entorno
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows

# Reinstalar
pip install -r requirements.txt
```

---

## Configuración Avanzada

### Aumentar Memoria de Spark

Si tienes más de 8 GB de RAM, editar `config.py`:

```python
SPARK_CONFIG = {
    "app_name": "Analisis_Clima_NOAA",
    "driver_memory": "8g",  # Cambiar de 4g a 8g
    "executor_memory": "8g",
    "log_level": "ERROR"
}
```

### Configurar Jupyter Notebook

```bash
# Ya viene en requirements.txt
# Para ejecutar:
jupyter notebook

# O con Docker:
docker-compose up jupyter
# Abrir http://localhost:8888
```

### Variables de Entorno Adicionales

Crear archivo `.env` (opcional):

```bash
# .env
SPARK_HOME=/path/to/spark
PYSPARK_PYTHON=python3
PYSPARK_DRIVER_PYTHON=python3
```

---

## Próximos Pasos

Una vez completada la instalación:

1. Ejecutar descarga de datos:
   ```bash
   python descargar_datos_noaa.py
   ```

2. Ejecutar análisis:
   ```bash
   python analisis_clima_pyspark.py
   ```

3. Revisar resultados en `resultados/`

---

## Recursos Adicionales

- [Documentación de PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Guía de Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Docker Documentation](https://docs.docker.com/)
- [NOAA Data Access](https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation)

---

Si continúas teniendo problemas, consulta el archivo README.md o contacta al equipo del proyecto.