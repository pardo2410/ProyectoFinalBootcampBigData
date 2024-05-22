### Documentación de Archivos del Proyecto

En esta carpeta se encuentran todos los archivos utilizados para generar los datasets que se procesaron en las diferentes etapas del proyecto. A continuación, se detalla el contenido de cada carpeta:

1. **Carpeta ICJ Inventario OC**:
    - Contiene los archivos asociados a las opiniones consultivas de 2004 y 2023.
    - Dentro de estas carpetas, se encuentran:
        - Opiniones consultivas (Advisory Opinions)
        - Procedimientos orales (Oral Proceedings)
        - Procedimientos escritos (Written Proceedings)

2. **Documentos Soporte Advisor Opinión ES**:
    - Contiene el resumen de las opiniones consultivas en español.
    - Incluye la opinión consultiva completa en español.

3. **Dataverse_file**:
    - Contiene el dataset de Harvard sobre las votaciones ordinarias de la Asamblea General.
    - Incluye archivos de soporte y el Codebook que explica detalladamente cada una de las variables.
    - Este documento fue utilizado para la etapa de visualización.
    - También se incluye la base de datos modificada que contiene información asociada a las opiniones consultivas utilizadas como casos de estudio.

4. **UN Votes Crawler**:
    - Contiene el crawler diseñado para extraer información de las resoluciones de votación de las Naciones Unidas desde la biblioteca digital de la ONU.
    - Su objetivo es navegar por la biblioteca digital, recoger URLs de las páginas de resoluciones de votación y extraer datos relevantes de cada resolución.
    - El enlace para acceder a la biblioteca digital de la ONU es: [Biblioteca Digital de la ONU](https://digitallibrary.un.org/search?ln=en&cc=Voting+Data&p=&f=&action_search=Search&rm=&sf=&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fti=0).

> 1. **Inicialización del WebDriver**:
    - Utiliza selenium para controlar un navegador Firefox.
    - Inicializa el driver y abre la URL objetivo para comenzar el proceso de extracción de datos.

> 2. **Extracción de URLs**:
    - Extrae todas las URLs de las resoluciones de votación desde las páginas de resultados.
    - Implementa una lógica de paginación para navegar a través de las páginas sucesivas hasta que no haya más páginas de resultados.

> 3. **Procesamiento de las Páginas de Resoluciones**:
    - Procesa cada URL para extraer información relevante usando lxml.
    - Abre y lee los archivos de las resoluciones almacenadas localmente para la extracción de datos.

> 4. **Almacenamiento de Datos**:
    - Almacena los datos procesados en un formato adecuado, para luego tratar el archivo y formatearlo en JSON, CSV o según se necesitara para el análisis posterior de la data.
    - No se hizo el formato de los datos inmediatamente para facilitar la toma de decisiones en pro al análisis y la visualización futura.
