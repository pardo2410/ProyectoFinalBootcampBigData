## Acerca de los Archivos Contenidos en el Repositorio

Este apartado contiene el análisis exploratorio realizado en Tableau. Se tomó como base para el análisis los datos mencionados de la base de datos de Harvard, localizados en la carpeta [dataverse_files](https://github.com/pardo2410/ProyectoFinalBootcampBigData/tree/main/01%20-%20Dataset/dataverse_files). Inicialmente, se realizó un preprocesamiento ([ProcesamientoDatasetUNVote.ipynb](https://github.com/pardo2410/ProyectoFinalBootcampBigData/blob/main/03%20-%20An%C3%A1lisis%20Exploratorio/ProcesamientoDatasetUNVote.ipynb)) de los datos contenidos en el archivo [UNVotes](https://github.com/pardo2410/ProyectoFinalBootcampBigData/blob/main/01%20-%20Dataset/dataverse_files/UNVotes.csv) de la carpeta `dataverse_files`. En este proceso, se ajustaron variables como los nombres de los países, se unificaron las votaciones y se generaron los registros faltantes para analizar la resolución de 2024.

### Archivo de Tableau: Analisis_Exploratorio

![image](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/126f072d-7af3-48b4-a6b0-061f2eee614c)

El archivo de Tableau llamado [`Analisis_Exploratorio`](https://public.tableau.com/shared/4N5CPXYZZ?:display_count=n&:origin=viz_share_link) está dividido en tres áreas principales:

1. **Selección de Tema y Resolución**:
   - A través de botones desplegables (dropdown), el usuario puede seleccionar un tema y una resolución asociada al mismo.
   - Las gráficas en la parte izquierda, incluyendo el mapamundi, mostrarán las votaciones de los países para dicha resolución.

2. **Indicadores de Votaciones**:
   - En el centro, los indicadores muestran los votos emitidos por los miembros permanentes y no permanentes del Consejo de Seguridad.
   - Adicionalmente, se pueden ver las votaciones de todos los estados miembros de las Naciones Unidas.

3. **Tablas de Distribución de Votaciones**:
   - A la derecha, se encuentran dos tablas:
     - La primera muestra la distribución global de las votaciones por tema.
     - La segunda desglosa esa votación global y permite conocer cómo votaron los miembros permanentes respecto a ese tema.

### Caso de Estudio

- Se presentan las votaciones de nuestro caso de estudio, mostrando las dos opiniones consultivas y sus votaciones.
- Se incluye la respuesta de la corte y su distribución en términos de los miembros permanentes del Consejo de Seguridad.

Este análisis permite una comprensión detallada de las votaciones y resoluciones, facilitando el estudio de las opiniones consultivas y su impacto en las decisiones internacionales.
