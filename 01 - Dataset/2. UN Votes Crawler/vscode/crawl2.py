# import requests
# from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import ast

def parse_url(url):
   
    driver = webdriver.Firefox()
    driver.get(url)
    result = driver.find_element(By.ID,"details-collapse")
    result = result.get_attribute("innerHTML")
    result = result + ""
   
    driver.close()
    return result
   
        
# def start():
f   = open("hrefs", mode="r", encoding="utf-8")
url = f.read()
url = ast.literal_eval(url)
numurl = len(url)
print("Cantidad de urls: "+str(numurl))
# url = url
# Llama a la función para analizar la URL
for u in url:
    parsed_tree = parse_url(u)

    # Haz algo con el árbol parseado, por ejemplo, imprimir el contenido
    if parsed_tree is not None:
        i = url.index(u)
        file = open("dowloads/contents_"+str(i),"w",encoding="utf-8")
        # file.write(etree.tostring(parsed_tree, pretty_print=True))
        # file.write(etree.tostring(parsed_tree[0], pretty_print=True))
        file.write(str(parsed_tree))
        file.close()
        if i%10==0:
            print("File printed -- "+str(i)+" elementos de "+str(numurl)+" totales")
        else:
            print("File printed")
        # print(etree.tostring(parsed_tree[0], pretty_print=True))
print("The End")
