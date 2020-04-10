# Web-scraping - Obtener información sobre el COVID-19

Se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer datos de la página: https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6, la cual tiene información actualizada sobre personas infectadas, fallecidas y recuperadas de COVID-19 a nivel mundial. 

## Comenzando 🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## Pre-requisitos 📋
Es necesario contar con lo siguiente: 
* Un IDE de su preferencia
* Python 3.7 o superior
* Git

## Instalación 🔧
Para ejecutar el script es necesario instalar las siguientes librerías:
```
pip install pandas
pip install selenium
pip install beautifulsoup4
pip install html5lib

```

## Ficheros del repositorio 📄
* web_scraping.py: El código para efectuar la extracción de las datos sobre COVID-19. 
* chromedriver.exe: Es el driver de Google Chrome 80 que se utiliza. Los drivers para otras versiones se pueden descargar de: https://chromedriver.chromium.org/downloads
* casos_paises_covid-19.csv: Es el Dataset con los datos obtenidos, cada vez que se ejecute el script se irán incorporando los datos al final del archivo. Los campos del Dataset son: países, fecha (de consulta), contagiados, fallecidos y recuperados.

## Ejecución⚙️
1. Descargue el código de GitHub mediante un fichero .zip o clone ejecutando el comando: git clone https://github.com/dcabrera1/Web-scraping.git
2. Ejecute el código con la ayuda de un IDE o ejecute el comando: python web_scraping.py
3. Verifique el archivo casos_paises_covid-19.csv con los datos actualizados a la fecha, los cuales se incluirán al final del archivo. 

## Versionado 📌
Usamos Git para el versionamiento. Para todas las versiones disponibles, mira los tags en este repositorio.

## Autores ✒️
* Paula Rodríguez
* David Cabrera

## Expresiones de Gratitud 🎁
El conjunto de datos fue obtenido de la página de ARGIS (https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6) perteneciente a Johns Hopkins University, que son expertos en salud pública, enfermedades infecciosas y preparación para emergencias. 
