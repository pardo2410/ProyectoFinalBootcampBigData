# Modelos de NLP para la Interpretación de Opiniones Consultivas de la Corte Internacional de Justicia

1. Instalación de librerías necesarias para el proceso de análisis
2. Carga del Dataset Consolidado UN - ICJ de las Opiniones Consultivas
   - Se emplea un conjunto de datos preparados a partir de los documentos digitalizados de la Corte Internacional de Justicia (ICJ).
4. Cardinalidad del Vocabulario y Análisis Exploratorio de los Datos.
   - Se encuentra análisis para determinar la diversidad y distribución de las clases dentro del dataset. Se utilizan funciones y gráficas para evaluar el balanceo de clases.
5. Implementación de diferentes modelos de NLP.
   - A. Modelo de Regresión Logística (Logistic Regression)
     El modelo de Regresión Logística se utiliza para la clasificación binaria. Calcula la probabilidad de que una observación pertenezca a una clase utilizando una función logística.
   - B. Modelo de Clasificación Gradient Boosting
     El modelo de Clasificación Gradient Boosting es un algoritmo de conjunto que combina múltiples árboles de decisión más débiles para construir un modelo predictivo más fuerte.
   - C. Modelo de Deep Learning RNN
     El modelo utiliza una red neuronal recurrente LSTM para procesar secuencias de texto, seguido de una capa densa de salida con activación sigmoide para clasificación binaria, y se compila con la función de pérdida de entropía cruzada binaria y el optimizador Adam.
   - D. Modelo de Regresión Logística TF-IDF:
     En este caso, implementaremos la técnica de TF-IDF (Term Frequency-Inverse Document Frequency) en el modelo de regresión logística. TF-IDF asigna pesos a palabras según su frecuencia en un documento y su rareza en el conjunto de documentos, destacando términos importantes en el análisis de texto.
   - E. Modelo Basado en BERT
     Bidirectional Encoder Representations from Transformers (BERT) es un modelo de lenguaje basado en transformadores que preentrena representaciones de texto bidireccionales para comprender mejor el contexto de las palabras en una oración. Este modelo es especialmente interesante para nosotros, dado el alto nivel técnico de las sentencias de la corte, ya que su tipo de análisis podría generar una representación más fiable del caso de estudio.
6. Evaluación del modelo BERT
   - A. Predicción para 2024
   - B. Implementación de modelo de Q&A
