# Procesamiento de archivos

El propósito principal de este proceso es extraer el texto contenido en los archivos PDF y almacenarlo en un formato adecuado para realizar operaciones de limpieza y análisis. Para lograr esto, se utiliza la biblioteca PyPDF2 para manipular los archivos PDF y extraer su contenido.

### Extracción de Texto de Archivos PDF

El proceso comienza abriendo un archivo PDF específico en modo de lectura binaria. Luego, se utiliza la biblioteca PyPDF2 para leer el contenido del PDF y almacenarlo en una estructura de datos adecuada para su procesamiento posterior.

### Segmentación de Opiniones Consultivas

Una vez que se ha extraído el texto de los archivos PDF, se procede a segmentar las opiniones consultivas en diferentes secciones para facilitar su análisis. Cada sección se guarda en un archivo separado en formato CSV para su posterior procesamiento.

### Limpieza de Archivos CSV

Después de la segmentación, se realiza una limpieza adicional de los archivos CSV generados anteriormente. Esto implica la eliminación de fragmentos no deseados o irrelevantes que puedan afectar el análisis posterior de los datos.

### Carga de Datos en Formato JSON

Finalmente, los datos limpios se cargan en archivos JSON para su posterior uso en el modelo de NLP. Cada archivo JSON contiene un conjunto de datos específico que corresponde a una pregunta particular en el contexto de las opiniones consultivas de la Corte Internacional de Justicia. Esta parte ya está debidamente explicada en la sección [Dataset](../01%20-%20Dataset/ContenidoDataset.md)

### Problemática ##

Debido a la forma en que se digitalizaron los documentos y la complicada estructura de los textos que contienen, tuvimos muchos problemas para extraer el contenido de forma fiable, generando caractéres inesperados que nos dificultó la tarea de limpieza. Este problema nos ralentizó demasiado el trabajo y tuvimos que buscar otra forma de extraer los datos. Finalmente decidimos extraer los fragmentos de los textos de forma manual diréctamente en JSON ya que al tratarse sólo de un tema en específico la cantidad de archivos a procesar era algo que podíamos asumir y dejamos la resolución de este problema para una tarea futura.

