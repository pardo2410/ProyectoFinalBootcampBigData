# [Reporte: Modelo BERT para Clasificación y Q&A](https://github.com/pardo2410/ProyectoFinalBootcampBigData/blob/main/05%20-%20Modelado/Modelo%20NLP%20Votaciones%20Naciones%20Unidas.ipynb)

## Resumen
Este reporte detalla la implementación y evaluación de un modelo BERT para clasificación de secuencias en un conjunto de datos judiciales, así como su aplicación en un modelo de Question & Answering (Q&A) para responder preguntas específicas relacionadas con las opiniones consultivas de la Corte Internacional de Justicia (CIJ).

## Implementación del Modelo BERT para Clasificación
El proceso de implementación del modelo BERT para clasificación se realizó siguiendo los siguientes pasos:

1. **Preprocesamiento de Texto**: Se realizó una limpieza básica del texto, convirtiendo el texto a minúsculas y eliminando signos de puntuación.
2. **Tokenización y Creación del Dataset**: Se utilizó la librería Transformers para tokenizar los datos y prepararlos para el entrenamiento del modelo.
3. **Entrenamiento del Modelo**: Se utilizó un modelo BERT preentrenado para la clasificación de secuencias, entrenado en un conjunto de datos judiciales.

El modelo fue entrenado durante 5 épocas, utilizando una estrategia de evaluación por pasos y una GPU para acelerar el proceso.

## Evaluación del Modelo BERT para Clasificación
El modelo BERT para clasificación mostró un rendimiento sobresaliente con una precisión del 95%, un recall perfecto del 100% y un F1-Score elevado del 96.97%. Además, la pérdida de entrenamiento y evaluación disminuyó de manera constante, indicando una convergencia efectiva del modelo. Sin embargo, la matriz de confusión reveló que el modelo cometió algunos errores en la clasificación de la clase 0.

Metricas:

![image](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/78845095-1796-4442-aa35-de8ed9fbf702)

Predicción 2024:

![image](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/45c6b97b-6093-4512-82a6-1519a0d745f4)


## Implementación del Modelo BERT para Q&A
Además de la clasificación, se implementó un modelo de Q&A utilizando BERT para responder preguntas específicas sobre las opiniones consultivas de la CIJ. El modelo fue capaz de generar respuestas precisas para preguntas complejas, utilizando el contexto proporcionado en el conjunto de datos.

Modelo:

![image](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/8e068c92-22ca-454f-9ea2-55e42058b5fd)

Salida:

![image](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/fba2d620-0bcf-4b23-b6b5-d4ce7ed87f00)

## Conclusiones y Recomendaciones
- El modelo BERT demostró ser altamente efectivo para la clasificación de secuencias en un contexto judicial.
- El modelo de Q&A también mostró un rendimiento prometedor en la generación de respuestas precisas.
- Se identificó la falta de tiempo para expandir el archivo de contexto como una limitación, lo que podría mejorar la precisión y relevancia de las respuestas del modelo.
- En términos generales, el modelo cumplió con nuestras expectativas para el análisis de los datos judiciales. Sin embargo, reconocemos la necesidad de enriquecerlo con una mayor cantidad de datos para asegurar que pueda generalizar de manera más precisa los casos negativos.
  
## Próximos Pasos
- Evaluar el modelo BERT con preguntas adicionales de las opiniones consultivas de la CIJ de 2024.
- Explorar formas de mejorar la precisión del modelo de Q&A mediante la expansión del archivo de contexto y ajustes adicionales en la arquitectura del modelo.
