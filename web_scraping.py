#Librerías
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import pandas as pd

# Google chrome 80
browser = webdriver.Chrome()

url = 'https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6'
browser.get(url)

# Defino un tiempo de espera hasta que se cargue la página
timeout = 20

# Espera hasta que se cargue la página para extraer todo el HTML
try:
    element_present = EC.presence_of_element_located((By.ID, 'ember1033'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    # Obtengo el html de la página
    soup = BeautifulSoup(browser.page_source, 'html5lib')
    # Cierro el navegador
    browser.close()


# Defino un diccionario para almacenarlo recuperado
dic_covid = {}

# Defino variables que se utilizarán
num_fallecidos = 0
num_recuperados = 0
num_contagiados = 0
nombre_pais = ""

# Obtengo la fecha actual de consulta
fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Recuperados
# Realizo una búsqueda por id y etiqueta span de la página
recuperados_html = soup.find(id='ember105').find_all("span")

for item in recuperados_html:
    p = item.find_all("p")
    if len(p) != 0:
        num_recuperados = p[0].span.strong.string.strip().replace('.', '')
        nombre_pais = p[1].get_text().strip()
        registro = {'fecha': fecha, 'contagiados': None, 'fallecidos': None,
                    'recuperados': num_recuperados}
        dic_covid[nombre_pais] = registro

# Fallecidos
# Realizo una búsqueda por id y etiqueta en la página
fallecidosHtml = soup.find(id='ember91').find_all("span")

for item in fallecidosHtml:
    p = item.find_all("p")

    if len(p) != 0:
        nombre_pais = p[1].get_text().strip()
        num_fallecidos = p[0].span.string.strip().replace('.', '')

        if(nombre_pais in dic_covid):
            dic_covid[nombre_pais]['fallecidos'] = num_fallecidos
        else:
            # Existen países que muestran los fallecidos por ciudades, se va a proceder a sumar los valores
            nombre_ciudad_pais = p[1].get_text().strip()
            
            # Existen países que no consta en la lista de recuperados por lo que se tienen que agregar a la lista           
            if(len(nombre_ciudad_pais.split()) == 1):
                registro = {'fecha': fecha, 'contagiados': None,
                            'fallecidos': num_fallecidos, 'recuperados': None}
                dic_covid[nombre_ciudad_pais] = registro
            else:
                # Obtengo únicamnete el nombre del país
                nombre_pais = nombre_ciudad_pais.split()[-1]
                num_temp = 0
                
                if(nombre_pais in dic_covid):
                    if(dic_covid[nombre_pais]['fallecidos'] != None):
                        num_temp = int(
                            dic_covid[nombre_pais]['fallecidos']) + int(num_fallecidos)
                        dic_covid[nombre_pais]['fallecidos'] = num_temp
                    else:
                        dic_covid[nombre_pais]['fallecidos'] = num_fallecidos
#Contagiados
# Realizo una búsqueda por id y etiqueta en la página
contagiados_Html = soup.find(id='ember34').find_all("span")

for item in contagiados_Html:
    p = item.find_all("p")
    if len(p) != 0:
        num_contagiados = p[0].span.strong.string.strip().replace('.', '')
        nombre_pais = p[1].get_text().strip()
        if(nombre_pais in dic_covid):
            dic_covid[nombre_pais]['contagiados'] = num_contagiados
        else:
                registro = {'fecha': fecha, 'contagiados': num_contagiados,
                            'fallecidos': None, 'recuperados': None}
                dic_covid[nombre_ciudad_pais] = registro

df = pd.DataFrame(dic_covid).transpose().rename_axis('paises')

df.to_csv('casos_paises_covid-19.csv', header=False,  mode='a')


