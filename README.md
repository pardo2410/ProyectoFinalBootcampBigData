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


