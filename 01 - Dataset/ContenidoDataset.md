# Documentación de Archivos del Proyecto

En esta carpeta se encuentran todos los archivos utilizados para generar los datasets que se procesaron en las diferentes etapas del proyecto. A continuación, se detalla el contenido de cada carpeta:

### 1. **Carpeta ICJ Inventario OC**:
- Contiene los archivos asociados a las opiniones consultivas de 2004 y 2023.
- Dentro de estas carpetas, se encuentran:
    - Opiniones consultivas (Advisory Opinions)
    - Procedimientos orales (Oral Proceedings)
    - Procedimientos escritos (Written Proceedings)

    #### **Documentos Soporte Advisor Opinion ES**:
    - Contiene el resumen de las opiniones consultivas en español.
    - Incluye la opinión consultiva completa en español.

### 2. **Segmented Files**:
Contiene las extracciones de los archivos originales de ICJ Inventario en formato JSON y/o texto plano.
- Los correspondientes a las opiniones consultivas están divididos por cada una de las respuestas de la Corte y por la opinión de cada juez.
- Los correspondientes a los procedimientos orales están divididos por las distintas participaciones de los portavoces de cada país en la Audiencia pública sobre la solicitud de opinión consultiva.
- Los procedimientos escritos no fueron procesados por la limitación de tiempo.

### 2. **Consolidated Files**:
Contiene la unificación de los diferentes archivos segmentados para su posterior uso en el modelo.

### 4. **Dataverse_file**:
- Contiene el dataset de Harvard sobre las votaciones ordinarias de la Asamblea General.
- Incluye archivos de soporte y el Codebook que explica detalladamente cada una de las variables.
- Este documento fue utilizado para la etapa de visualización.
- También se incluye la base de datos modificada que contiene información asociada a las opiniones consultivas utilizadas como casos de estudio.

### 5. **UN Votes Crawler**:
- Contiene el crawler diseñado para extraer información de las resoluciones de votación de las Naciones Unidas desde la biblioteca digital de la ONU.
- Su objetivo es navegar por la biblioteca digital, recoger URLs de las páginas de resoluciones de votación y extraer datos relevantes de cada resolución.
- El enlace para acceder a la biblioteca digital de la ONU es: [Biblioteca Digital de la ONU](https://digitallibrary.un.org/search?ln=en&cc=Voting+Data&p=&f=&action_search=Search&rm=&sf=&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fti=0).

    #### **Inicialización del WebDriver**:
    - Utiliza selenium para controlar un navegador Firefox.
    - Inicializa el driver y abre la URL objetivo para comenzar el proceso de extracción de datos.

    #### **Extracción de URLs**:
    - Extrae todas las URLs de las resoluciones de votación desde las páginas de resultados.
    - Implementa una lógica de paginación para navegar a través de las páginas sucesivas hasta que no haya más páginas de resultados.

    #### **Procesamiento de las Páginas de Resoluciones**:
    - Procesa cada URL para extraer información relevante usando lxml.
    - Abre y lee los archivos de las resoluciones almacenadas localmente para la extracción de datos.

    #### **Almacenamiento de Datos**:
    - Almacena los datos procesados en un formato adecuado, para luego tratar el archivo y formatearlo en JSON, CSV o según se necesitara para el análisis posterior de la data.
    - No se hizo el formato de los datos inmediatamente para facilitar la toma de decisiones en pro al análisis y la visualización futura.
