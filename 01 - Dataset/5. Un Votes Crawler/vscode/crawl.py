# import requests
# from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def parse_url(url):
    # Realiza una solicitud GET a la URL
    # response = requests.get(url)
    
    # # Verifica si la solicitud fue exitosa
    # if response.status_code == 200:
    #     # Parsea el contenido HTML/XML utilizando lxml
        # parser = etree.HTMLParser()
        # tree = etree.fromstring(response.content, parser)
        # app_root_element = tree.find(".//body")
        # return tree
         # Verifica si se encontró el elemento
        # if app_root_element is not None:
            # Obtiene el contenido del elemento
            # content = etree.tostring(app_root_element, method='html', encoding='utf8')
            # return content
            # toClick = tree.findall('''.//div[class='result-title']''')
            # toClick = tree.find(".//input#mobilecheckbox2-fct__8-86")
            # return toClick
    driver = webdriver.Firefox()
    driver.get(url)
    # Esperar a que los elementos se carguen completamente (por ejemplo, esperar a que el primer elemento aparezca)
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "result-title")))
    final = []
    next_bool  = True
    while next_bool:
        elem = driver.find_elements(By.CLASS_NAME, "result-title")
        # for e in elem:
        #     final.append(e)    
        # return final
        # print(type(elem))
        for e in elem:
            # e.click()
            # e = driver.find_element(By.ID, "details-collapse")
            p = e.find_element(By.TAG_NAME, "a")
            final.append(p.get_attribute("href"))
            print(final)
            # driver.get(url)
        try:
            url_after = driver.current_url
            next_  = driver.find_element(By.CLASS_NAME,"rec-navigation")
            next_1 = next_.find_elements(By.TAG_NAME ,"a")
            next_1[len(next_1)-1].click()

            url_before = driver.current_url
            if url_after == url_before:
                next_bool = False
            else:
                next_bool = True

        except:
            next_bool = False
        
    driver.close()
    return final
    
    # else:
        # return "No se encontró el elemento <body>."
# Encuentra el elemento con el atributo app-root
# app_root_element = tree.cssselect('body')
# app_root_element = tree.xpath('//*[@app-root]')
    
    # Verifica si se encontró el elemento
# if app_root_element:
    # Obtiene el contenido del elemento
    # content = etree.tostring(app_root_element[0], method='html', encoding='unicode')
    # return content
# else:
    # return "No se encontró ningún elemento con el atributo 'app-root'."
    # else:
        # print("Error al obtener la URL:", response.status_code)
    # return None

# URL que quieres analizar
url = "https://digitallibrary.un.org/search?ln=en&cc=Voting+Data&p=&f=&action_search=Search&rm=&sf=&so=d&rg=50&c=Voting+Data&c=&of=hb&fti=0&fti=0"

# Llama a la función para analizar la URL
parsed_tree = parse_url(url)

# Haz algo con el árbol parseado, por ejemplo, imprimir el contenido
if parsed_tree is not None:
    file = open("hrefs","w",encoding="utf-8")
    # file.write(etree.tostring(parsed_tree, pretty_print=True))
    # file.write(etree.tostring(parsed_tree[0], pretty_print=True))
    file.write(str(parsed_tree))
    file.close()
    print("File printed")
    import crawl2
    crawl2.start()
    # print(etree.tostring(parsed_tree[0], pretty_print=True))
