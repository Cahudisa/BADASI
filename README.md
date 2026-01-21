# BADASI: Base de Datos Automatizada para Sismología

Este repositorio contiene el desarrollo del proyecto de grado **BADASI**, cuyo objetivo es diseñar e implementar un sistema automatizado para el procesamiento, almacenamiento y gestión de metadatos sísmicos, orientado a facilitar su análisis y reutilización en estudios posteriores.

El proyecto integra técnicas clásicas de detección de eventos sísmicos con herramientas modernas de manejo de datos, permitiendo construir un flujo de trabajo reproducible, escalable y organizado.

---

## Descripción general del proyecto

En sismología, el análisis de grandes volúmenes de datos requiere no solo métodos confiables de detección de eventos, sino también estructuras adecuadas para almacenar y consultar la información generada. BADASI aborda este problema mediante:

- La detección automática de eventos sísmicos y segmentos de ruido.
- La organización de metadatos en una base de datos local.
- La automatización del flujo desde datos crudos hasta datasets estructurados.

El sistema fue diseñado con un enfoque modular, de forma que pueda adaptarse a diferentes conjuntos de datos y ampliarse en futuros trabajos.

---

## Objetivos principales

- Desarrollar un procedimiento sistem´atico de recolección y depuración de trazas sísmicas provenientes de la REDNE.
- Implementar y automatizar un pipeline de procesamiento de datos sísmológicos.
- Diseñar y estructurar una base de datos sismol´ogica inspirada en la organización del Stanford Earthquake Dataset (STEAD).
- Integrar y escalar un sistema de automatizaci´on para la actualización continua del dataset.
- 
---

## Metodología

El flujo general del sistema incluye las siguientes etapas:

1. **Preprocesamiento de datos sísmicos**  
   Lectura y preparación de registros en formato estándar (MiniSEED / HDF5).

2. **Detección automática de eventos**  
   Aplicación del algoritmo STA/LTA para identificar incrementos significativos de energía asociados a eventos sísmicos.

3. **Generación de metadatos**  
   Extracción de información relevante de cada evento y de ventanas de ruido.

4. **Almacenamiento en base de datos**  
   Inserción de metadatos en una base de datos MongoDB, con control de versiones y acceso por roles.

5. **Consulta y exportación**  
   Acceso a la información mediante consultas filtradas y exportación a formatos como CSV y JSON.

---

## Base de datos

El sistema utiliza **MongoDB** como gestor de base de datos local debido a su flexibilidad para manejar datos semiestructurados.  
La base de datos se organiza en colecciones separadas para:

- Metadatos de eventos sísmicos.
- Metadatos de ruido.
- Versiones históricas de los documentos.

Este diseño permite mantener un historial de cambios y asegurar la integridad de la información a lo largo del tiempo.

---

## Tecnologías utilizadas

- **Python**: procesamiento de datos y automatización del pipeline.
- **ObsPy**: manejo y análisis de datos sísmicos.
- **MongoDB**: almacenamiento y gestión de metadatos.
- **HDF5 / CSV / JSON**: formatos de entrada y salida.
- **Git & GitHub**: control de versiones y documentación del proyecto.

---

## Estructura general del repositorio

```text
├── data/               # Datos de entrada y salida (no incluidos por defecto)
├── scripts/            # Scripts de procesamiento y automatización
├── database/           # Scripts relacionados con MongoDB
├── figures/            # Figuras utilizadas en la documentación
├── docs/               # Documentación adicional del proyecto
└── README.md           # Descripción general del proyecto
