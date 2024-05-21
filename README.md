# Proyecto Final de Bootcamp: Big Data, Machine Learning y AI

En el proceso de investigación, decidimos abordar el análisis de las votaciones nominales en la Asamblea General de la ONU desde 1946 hasta 2024. Nos centramos en el comportamiento de las votaciones en referencia a problemáticas de alta importancia a nivel mundial, tales como:

- Votos relacionados con el conflicto palestino (19%)
- Votos relacionados con armas nucleares y material nuclear (13%)
- Votos relacionados con el control de armas y el desarme (16%)
- Votos relacionados con el colonialismo (18%)
- Votos relacionados con los derechos humanos (17%)
- Votos relacionados con el desarrollo económico (9%)

Partimos del dataset creado por la Harvard University DataVerse y el repositorio denominado [United Nations General Assembly Voting Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=hdl%3A1902.1%2F12379).

Debido a la relevancia del tema, decidimos enfocarnos en las votaciones asociadas al conflicto palestino y, específicamente, en las opiniones consultivas relacionadas con este asunto. 

Después de investigar, encontramos que la Asamblea General de las Naciones Unidas puede remitir cierto tipo de preguntas a las instituciones miembros para recibir valoraciones expertas sobre temas como salud, economía o derecho internacional, entre otros. Por tanto, enfocamos nuestros esfuerzos en realizar un análisis de NLP utilizando documentos asociados a la opinión consultiva de 2004 ([A/ES-10/273](https://documents.un.org/doc/undoc/gen/n04/419/86/pdf/n0441986.pdf?token=Vp4AGGksBar61a46IO&fe=true)), donde la Asamblea solicitaba a la CIJ dar respuesta a la siguiente pregunta:

> ¿Cuáles son las consecuencias jurídicas que se derivan de la construcción del muro que levanta Israel, la Potencia ocupante, en el territorio palestino ocupado, incluida Jerusalén oriental y sus alrededores, según se describe en el informe del Secretario General, teniendo en cuenta las normas y principios de derecho internacional, incluido el Cuarto Convenio de Ginebra de 1949 y las resoluciones pertinentes del Consejo de Seguridad y de la Asamblea General?

Utilizamos como base para el entrenamiento los alegatos escritos ([Written Proceedings](https://www.icj-cij.org/index.php/case/131/written-proceedings)), alegatos orales ([Oral Proceedings](https://www.icj-cij.org/index.php/case/131/oral-proceedings)), la opinión consultiva ([Advisory Opinions](https://www.icj-cij.org/index.php/case/131/advisory-opinions)) y las opiniones separadas ([Separate Opinions](https://www.icj-cij.org/index.php/case/131/advisory-opinions)) de los jueces, con el fin de proporcionar suficiente información y contexto al modelo para realizar el proceso de inferencia.

A continuación, se presenta el diagrama de flujo asociado al proceso de generación de una opinión consultiva. Este proceso abarca desde la solicitud inicial en la Asamblea General, su posterior procesamiento en la Corte Internacional de Justicia (CIJ), hasta su retorno para la votación de aceptación por parte de la Asamblea General de las Naciones Unidas.

![Screenshot workflow UN   ICJ](https://github.com/pardo2410/ProyectoFinalBootcampBigData/assets/10873597/966d07c9-2749-4289-82ad-e3c271d1576f)

## Objetivo del Modelo

El objetivo principal del modelo es predecir, a través de un análisis de sentimiento, cuál será el resultado asociado a las votaciones de la opinión consultiva ([A/Res/77/247](https://n2300468.pdf)). Esta opinión consultiva, que actualmente está en curso en la Corte Internacional de Justicia, busca dar respuesta a dos preguntas relacionadas con el fallo de 2004:

a) ¿Cuáles son las consecuencias jurídicas que se derivan de que Israel continúe violando el derecho del pueblo palestino a la libre determinación, de sus prolongados actos de ocupación, asentamiento y anexión del territorio palestino ocupado desde 1967, incluidas las medidas destinadas a alterar la composición demográfica, el carácter y el estatuto de la Ciudad Santa de Jerusalén, y de la aprobación por Israel de legislación y medidas discriminatorias conexas?

b) ¿Cómo afectan las políticas y prácticas de Israel mencionadas en el párrafo 18 a) al estatuto jurídico de la ocupación y qué consecuencias jurídicas se derivan de ese estatuto para todos los Estados y para las Naciones Unidas?

Para ello, ampliamos el modelo agregando los alegatos [orales](https://www.icj-cij.org/case/186/oral-proceedings) y [escritos](https://www.icj-cij.org/case/186/written-proceedings) correspondientes a la opinión consultiva de 2024.

El modelo seleccionado para realizar el análisis es BERT (Bidirectional Encoder Representations from Transformers). BERT está diseñado para entender el contexto de una palabra en una frase leyendo en ambas direcciones (izquierda a derecha y derecha a izquierda). Esto permite una comprensión más precisa del lenguaje natural, lo cual es esencial para interpretar textos legales complejos como las opiniones consultivas.

Adicionalmente, decidimos implementar un modelo de Preguntas y Respuestas (Q&A) basándonos en la salida del modelo BERT para responder las preguntas teniendo en cuenta la información suministrada en los corpus.


