1. **Análisis General de la Data**:
    - **Dataset Utilizado**: Se emplea un conjunto de datos preparados a partir de los documentos digitalizados de la Corte Internacional de Justicia (ICJ).
    - **Análisis de Cardinalidad y Balanceo de los Datos**: Se encuentra análisis para determinar la diversidad y distribución de las clases dentro del dataset. Se utilizan funciones y gráficas para evaluar el balanceo de clases.
    - **Ngramas y Nube de Palabras**: Se realiza una exploración de los textos gracias a la herramienta de `ngrams` y `wordclouds`, así pudiendo identificar patrones de palabras y frases. Esto hecho por dos cosas: primero, con el fin de verificar el estado de la data, viendo de una manera eficiente si se requiere de mejor preprocesamiento y recurrir a un correcto proceso iterativo; segundo, para entender de manera sencilla de qué es lo que predomina en la data.
    
    - **Word Embeddings**: En el nootebook se describe la generación de embeddings de palabras usando la librería `Word2Vec`, sirviendo no solo como una herramienta para la extracción de características textuales, sino también un medio para explorar y visualizar la semántica del vocabulario.

     ## Inicialización y Entrenamiento de Word2Vec

      1. **Definición de Parámetros y Inicialización del Modelo**:
      - Se establecen parámetros específicos para el modelo Word2Vec, tales como el tamaño del vector, el contexto de ventana, y la frecuencia mínima de palabras entre otros. Estos parámetros definen las características del espacio vectorial y la operación del algoritmo.
      - Se inicializa el modelo Word2Vec con estos parámetros y se construye el vocabulario a partir de un corpus preprocesado, que es una lista de tokens extraída de las columnas de texto del DataFrame.

      2. **Entrenamiento del Modelo**:
      - El modelo es entrenado sobre el corpus por un total de 10 épocas, parámetro escogido por haber sido encontrado como el más óptimo según las características del corpus

     ## Operaciones Post-Entrenamiento

      3. **Guardado y Carga del Modelo**:
      - Después del entrenamiento, el modelo es guardado en un archivo `w2v_sg_model.pkl`, permitiendo reutilizar los embeddings sin necesidad de reentrenar.

      4. **Validación del Modelo**:
      - Se valida la efectividad del modelo utilizando una función `print_sim_words` que imprime las palabras más similares a una palabra dada.

     ## Visualización de Embeddings

      5. **Visualización en 2D**:
      - Para una interpretación visual y se realiza una gráfica en dos dimensiones de los embeddings. Se seleccionan palabras clave relacionadas con el contexto y se extraen sus embeddings más similares, mostrando cómo palabras semánticamente similares se agrupan juntas.

2. **Preprocesamiento**:

     Se utiliza la librería de `nltk` para el preprocesamiento del corpus.

     1. **Inicialización de Herramientas de Procesamiento**:
     - **Para Tokenizador**: Usado `RegexpTokenizer` con una expresión regular que selecciona solo caracteres alfanuméricos.
     - **Para Stop-Words**: Carga una lista de stopwords del inglés.
     - **Para Lematización**: Usado `WordNetLemmatizer` para convertir las palabras a su forma base o lema.

     2. **`nltk_cleaner`**:
     - **Manejo de Texto Nulo**: Retorna una cadena vacía si el texto de entrada es nulo.
     - **Normalización de Texto**: Aplica normalización Unicode.
     - **Tokenización y Limpieza**: Descompone el texto en palabras.
     - **Tratamiento de Stop Words y Lematización**: Cada token se lematiza y se verifica contra la lista de stopwords.
     - **Conversión de Números**: Usado `num2words` para que los dígitos se conviertan a palabras. 

3. **Modelo de Deep Learning**:
