# Arquitectura

## Diseño del DAaaS

### Definición de la estrategia del DAaaS

Crear un aplicación web que mejore el acceso a la información de los asuntos tratados por Naciones Unidas optimizando el proceso de difusión de los problemas universales de la humidad.
La aplicación permitirá buscar, visualizar y consultar sobre cualquiera de los temas tratados por las UN, y predecirá las resoluciones en base a los documentos y recomendaciones de otra entidades descentralizadas.
Adicionalmente notificará cada nueva resolución, opiniones y votaciones a los suscriptores del servicio.

### Arquitectura DAaaS

Fuentes de datos
- Datasets 
	- Biblioteca de digital de la Naciones Unidas
	- United Nations General Assembly Voting Data 
	- Documentos de Corte internacional de Justica Advisory proceedings
	- Documentos de Corte internacional de Justica Written Proceedings
	- Documentos de Corte internacional de Justica Oral Proceedings
	- Documentos de Corte internacional de Justica Advisory Opinions
  - [https://digitallibrary.un.org/](https://digitallibrary.un.org/?ln=en)
  - [https://dataverse.harvard.edu/dataset.xhtml?persistentId=hdl:1902.1/12379](https://dataverse.harvard.edu/dataset.xhtml?persistentId=hdl:1902.1/12379)
  - [https://www.icj-cij.org/advisory-proceedings](https://www.icj-cij.org/advisory-proceedings)
  - [https://www.icj-cij.org/case/131/written-proceedings](https://www.icj-cij.org/case/131/written-proceedings)
  - [https://www.icj-cij.org/case/131/oral-proceedings](https://www.icj-cij.org/case/131/oral-proceedings)
  - [https://www.icj-cij.org/case/131/advisory-opinions](https://www.icj-cij.org/case/131/advisory-opinions)
- Crawler y Scrapper sobre las votaciones
Componentes
- Google Cloud Storage para ficheros de Crawler, Scrapper, dataset, pdf, txt 
- Server de aplicación Web
 - Servidor web nginx
 - Aplicación Angular
- Server de aplicación Chat Web
 - Aplicación Streamlit Chat
 - Configurar retención de logs para análisis en caso de ser necesario
- Server de aplicación API REST
  - Servidor web nginx
  - Aplicación en Python/Flask
  - Configurar retención de logs para análisis en caso de ser necesario
- Firewall para el control de acceso a recursos
- Load Balancer para la gestion de peticiones http / https
- Base de datos Google Cloud SQL
- Base de datos Chroma DB
- Cloud Functions para crawlers, scrappers, programas python
- Cloud Scheduler para la ejecución de tareas programadas
- DataPrep para las transformaciones de data para el Datawarehouse
- Big Query para Datawarehousing
- Firebase Cloud Messaging para las notificaciones push
- ElasticSearch y Kibana para análisis de logs de trafico, guardrails requerimientos y performance los servicios
  
### DAaas Operation Model Design and Rollout
- Tareas por unica vez al inicio del proyecto
  - Crear y configurar un Google Cloud Project "UNVotes" con un bucket de Cloud Storage
  - Obtener los Datasets de votaciones de 1946 a 2024
    - Descargar los archivos .pdf desde [https://digitallibrary.un.org/?ln=en](https://digitallibrary.un.org/?ln=en)
    - Crear Crawler y scraper de recopilación de datos y documentos futuros denominarlos CF_CR_SC_Data y CF_CR_SC_Documents
      - Estos script deberán dejar los resultados de su ejecución en Cloud Storage en las carpetas y archivos con el siguiente formato /in/Data/document.json, /in/Data/document.pdf, /in/Data/document.csv y /in/[DOCUMENTS]/YYYYMMDD.* respectivamente además de volcar los datos a la BD en Cloud SQL y procesarlos documentos para volcarlos a las base de datos vectorial Chroma DB
    - Probar la ejecución del programa para el procesamiento de los archivos
    - Subirlo como una Cloud function para su posterior ejecución de actualización de datos
  - Obtener los Datasets históricos
    - Descargar los archivos .pdf de los sitios de la CIJ https://www.icj-cij.org
    - Analizar y validar las estructuras de los mismo, normalizar los datos y generar el script para procesarlos
    - Procesar los archivos para generar los scripts SQL de creación de tablas e inserción de datos en Cloud SQL denominarlos scripts_01.1_creation_tables.sql y scripts_01.2_load_data.sql
    - Subir los scripts sql a Google Cloud Storage para su posterior ejecución manualmente
  - Crear la base de datos BD en Sql Cloud
  - Crear la base de datos DB Chroma DB (montando una maquina virtual si GCP no la tuviera disponible)
  - Procesar los scripts generados on premise en la BD de SQL Cloud
    - de creación de tablas denominado scripts_01.1_creation_tables.sql
    - de la inserción de los datos históricos scripts_01.2_load_data.sql
  - Subir los scripts scripts_01.* a Google Cloud Storage en la carpeta /scripts_01_creation_load en caso de necesitar reprocesarlos datos

  - Crear Crawlwer y scraper en Python de recopilación de datos mensuales y subirlo como una Cloud function denominado CF_CR_SC_Monthly
    - El script deberá dejar el resultado de su ejecución en Cloud Storage en las carpetas y archivos con el siguiente formato /in/monthly/[tipo-document]/YYYYMM.* , donde el * representa a .pdf, .txt .csv
  - Crear Crawlwer y scraper de recopilación de datos diarios y subirlo como una Cloud function denominado CF_CR_SC_Daily
    - El script deberá dejar el resultado de su ejecución en Cloud Storage en las carpetas y archivos con el siguiente formato /in/daily/[tipo-document]/<document>.* , donde el * representa a .pdf, .txt .csv
  - Crear usuarios para ejecutar los Cloud functions y asignar los permisos correspondientes
  - Configurar Cloud Scheduler para la ejecución de las tareas programadas
    - Los scripts CF_CR_SC_Advisory, CF_CR_SC_Written, CF_CR_SC_Oral y CF_CR_SC_Opinion de recopilacion de datos de establecimientos y productos (planificación mensual días 1,3,5,7,10 hora 11 PM)
    - El script CF_CR_SC_Monthly de recopilación de datos mensual (planificación mensual días 1,3,5,7,10 hora 11 PM GTM)
    - El script CF_CR_SC_Daily de recopilación de nuevos documentos (planificación diaria hora 6 AM GTM) 
  - Crear la base de datos BDW para Datawarehousing
  - Configuración de Dataprep para la generación del Datawarehouse en BigQuery
    - Crear los jobs para la generación de datos que serán usados para las predicciones, análisis, etc.
    - Probar la ejecución de los jobs
    - Programar la ejecución de los jobs
  -  Crear las instancias para el servidor Web, API y Streamlit
    -  Instalar el servidor Web
    -  Instalar la aplicación Angular, API y Streamlit según corresponda
    -  Configurar los archivos de log para que se almacén en cloud Storage en las carpetas /logging/[server]/YYYYMMDD  y /logging/[server]/GYYYYMMDD para guardrails

  -  Configurar las reglas de firewall para permite el acceso a las aplicaciones Angular, API y Streamlit
  - Firebase
    - Crear la aplicación y configurar las notificaciones
  - Notificaciones
    - Crear los Cloud functions CF_Notifications
    - Programar la ejecución de los jobs
    - Probar realizar el tunning de los jobs
  - Predicciones
    - Crear los Cloud functions CF_Predicciones con los modelos utilizando el modelo pre-entrenado para una rápida y efectiva como un MVP de esta feature 
    - Programar la ejecución de los jobs
    - Probar realizar el tunning de los jobs

- Tareas para realizar luego de la puesta en marcha
  - Analítica de performance de la aplicación, análisis de errores, análisis de las peticiones https
    - Configurar una instancia del servidor para Elastic y Kibana
    - Configurar los indices necesarios acordes a la información a analizar
    - Implementar los dashboard para conocer la performance de la aplicación, detecciones de errores, análisis de trafico e información solicitada 
    - Crear los Cloud functions CF_Subir_Logs para subir los logs a Elastic
    - Programar la ejecución de los CF_Subir_Logs
  - Configurar las reglas de firewall para permite el acceso a Kibana

- Tareas para realizar mensualmente
  - Análisis que los costos vs el desempeño de la solución para que este de acuerdo a lo previsto de inversión.
  - Buscar oportunidades de mejora y realizar la reingeniería que sea necesaria si se encuentran desviaciones
  
### DAaas Diagram

[Diagrama](Diagrama.drawio)

![Diagrama](Diagrama.png)
