from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pandas as pd 
import time

# TRATAMENTO DE EXCEÇÃO
from selenium.common.exceptions import TimeoutException

# CAMINHO DO CHROME DRIVER
chrome_driver = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# CONFIGURAÇÃO DO SIMULADOR
service = Service(chrome_driver)
controle = webdriver.ChromeOptions()
controle.add_argument("--desable-gpu")
controle.add_argument("--window-size=1920, 1080")

# INICIA O WEBDRIVER
driver = webdriver.Chrome(service=service, options=controle)

# DEFINE URL ONDE SERÁ REALIZADO A ANÁLISE
url = "https://masander.github.io/AlimenticiaLTDA/#/humanresources"
driver.get(url) # EXECUTAR A URL
time.sleep(5)

nav = driver.find_element(By.CLASS_NAME, "subpage_button")
buttons = nav.find_elements(By.TAG_NAME, "button")

botao_proximo = buttons[2]
botao_proximo.click()
time.sleep(5)

dic_turno = {"Turno": [], "Entrada": [], "Saida": []}

turnos = driver.find_elements(By.XPATH, "//table/tbody//tr")

for turno in turnos:
    try:
        periodo = turno.find_element(By.CLASS_NAME, "td_Turno").text
        entrada = turno.find_element(By.CLASS_NAME,"td_Entrada").text
        saida = turno.find_element(By.CLASS_NAME,"td_Saída").text
        print(f"{turno} - {entrada} - {saida}")

        dic_turno["Turno"].append(periodo)
        dic_turno["Entrada"].append(entrada)
        dic_turno["Saida"].append(saida)
    except Exception as e:
        print("Erro: ", e)

driver.quit()

df = pd.DataFrame(dic_turno)
df.to_excel("turnos.xlsx", index=False)