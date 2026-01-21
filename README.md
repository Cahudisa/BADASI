BADASI: Base de Datos Sismológica de la REDNE
Trabajo de Grado para optar al título de Ingeniero Electrónico > Universidad Industrial de Santander (UIS)

Este repositorio contiene el código fuente y la documentación para el diseño y automatización de una base de datos sismológica para la Red Sismológica del Nororiente Colombiano (REDNE). El proyecto implementa un pipeline completo de procesamiento de datos que transforma registros crudos en un dataset estructurado (inspirado en STEAD), listo para el entrenamiento de modelos de Inteligencia Artificial.

Tabla de Contenidos
Descripción del Proyecto

Arquitectura y Flujo de Trabajo

Características Principales

Estructura del Repositorio

Instalación y Requisitos

Uso

Autores y Agradecimientos

Descripción del Proyecto
La sismología moderna genera terabytes de datos, pero gran parte de esta información se encuentra dispersa o en formatos crudos que dificultan su uso en investigación avanzada. Este proyecto soluciona ese problema para la región de Santander (Nido Sísmico de la Mesa de los Santos) mediante la creación de una infraestructura automatizada.

El sistema es capaz de:


Recolectar automáticamente trazas sísmicas desde el Servicio Geológico Colombiano (SGC) y OSSO.


Depurar señales, corrigiendo errores instrumentales y saturaciones.


Detectar eventos sísmicos y ruido utilizando un algoritmo STA/LTA adaptativo.


Almacenar la información en un esquema híbrido: MongoDB para metadatos y HDF5 para formas de onda.


Arquitectura y Flujo de Trabajo
El proyecto sigue un esquema secuencial de procesamiento de datos para garantizar la trazabilidad:

Fragmento de código

graph LR
A[Datos Crudos SGC/OSSO] --> B(Preprocesamiento y Limpieza)
B --> C{Detector STA/LTA Adaptativo}
C -->|Evento Confirmado| D[Recorte y Alineación]
C -->|Ruido Validado| E[Dataset de Ruido]
D --> F[(Base de Datos HDF5 + MongoDB)]
E --> F
Nota: El flujo detallado incluye la descarga de archivos .mseed, la conversión de canales (redundancia UIS05) y la generación de metadatos estandarizados.

Características Principales:

Adquisición Automatizada: Scripts que consultan catálogos sísmicos y descargan ventanas de tiempo específicas sin intervención manual.

Detector Inteligente (STA/LTA): Algoritmo que ajusta sus umbrales dinámicamente. Aumenta la sensibilidad para sismos tenues y se vuelve estricto ante ruido urbano para reducir falsos positivos.



Gestión de Ruido: Generación de un subconjunto de "no-eventos" (ruido ambiental) validado, fundamental para entrenar redes neuronales robustas.


Estandarización: Datos organizados bajo los lineamientos de STEAD y SeisBench, facilitando la interoperabilidad científica.


Base de Datos NoSQL: Uso de MongoDB para consultas flexibles y control de versiones de metadatos.


Estructura del Repositorio
Plaintext

BADASI/
├── A_REDNE_mseed_downloads/      # Descargas crudas iniciales
├── B_REDNE_mseed_UIS05virtual/   # Corrección de canales (UIS05)
├── C_Valid_mseed_files/          # Archivos validados (longitud correcta)
├── D_REDNE_mseed_tendencia_media/# Trazas sin tendencia (Preprocesadas)
├── E_mseed_eventos_finales/      # Eventos recortados y detectados
├── REDNE_plantilla.hdf5          # Dataset final consolidado
├── src/                          # Código fuente (Scripts Python)
│   ├── download_data.py          # Script de adquisición
│   ├── preprocess.py             # Limpieza y corrección
│   ├── sta_lta_detector.py       # Algoritmo de detección
│   └── database_manager.py       # Conexión con MongoDB
├── environment.yml               # Archivo de entorno Conda
└── README.md                     # Documentación
Instalación y Requisitos
Este proyecto fue desarrollado utilizando Python 3.7.16. Se recomienda usar conda para gestionar las dependencias.

Prerrequisitos
Anaconda o Miniconda

MongoDB Community Server (local o Atlas)

Configuración del Entorno
Clonar el repositorio:

Bash

git clone https://github.com/Cahudisa/BADASI.git
cd BADASI
Crear el entorno virtual con las dependencias necesarias (ObsPy, Pandas, PyMongo, h5py):

Bash

conda env create -f environment.yml
conda activate badasi_env
🛠️ Uso
El pipeline se ejecuta de manera secuencial. A continuación se describen los pasos generales:

Descarga de Datos: Ejecuta el script de consulta para obtener los archivos .mseed del periodo deseado (configurado en el script para 2024-2025).

Bash

python src/download_data.py
Preprocesamiento: Realiza la corrección instrumental, duplicación de canales virtuales y eliminación de tendencia.

Bash

python src/preprocess.py
Detección de Eventos: Corre el algoritmo STA/LTA adaptativo para clasificar sismos y ruido.

Bash

python src/sta_lta_detector.py
Generación de Base de Datos: Consolida los resultados en el archivo HDF5 y sube los metadatos a MongoDB.

Bash

python src/database_manager.py
Autores y Agradecimientos
Autor:


Carlos Humberto Díaz Salazar - Ingeniería Electrónica, UIS - GitHub.

Dirección:

Dr.-Ing. Sergio Alberto Abreo Carrillo (Director).

Ph.D. Ana Beatriz Ramírez Silva (Co-Directora).

Agradecimientos:

A la Universidad Industrial de Santander (UIS) y la Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones.

Al Grupo de Investigación CPS.

Al Servicio Geológico Colombiano (SGC) y OSSO por la disponibilidad de los datos.
