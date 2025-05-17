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

botao_proximo = buttons[0]
botao_proximo.click()
time.sleep(5)

dic_frequencia = {"Id_funcionario": [], "Data": [], "Entrada": [], "Saida": [], "Faltou": [], "Horas_extras": []}

frequencias = driver.find_elements(By.XPATH, "//table/tbody//tr")

for frequencia in frequencias:
    try:
        id_funcionario = frequencia.find_element(By.CLASS_NAME, "td_id_funcionario").text.strip()
        data = frequencia.find_element(By.CLASS_NAME,"td_data").text.strip()
        entrada = frequencia.find_element(By.CLASS_NAME,"td_entrada").text.strip()
        saida = frequencia.find_element(By.CLASS_NAME,"td_saida").text.strip()
        faltou = frequencia.find_element(By.CLASS_NAME,"td_faltou").text.strip()
        horas_extras = frequencia.find_element(By.CLASS_NAME,"td_horas_extras").text.strip()

        print(f"{id_funcionario} - {data} - {entrada} - {saida} - {faltou} - {horas_extras}")

        dic_frequencia["Id_funcionario"].append(id_funcionario)
        dic_frequencia["Data"].append(data)
        dic_frequencia["Entrada"].append(entrada)
        dic_frequencia["Saida"].append(saida)
        dic_frequencia["Faltou"].append(faltou)
        dic_frequencia["Horas_extras"].append(horas_extras)
    except Exception as e:
        print("Erro: ", e)

driver.quit()

df = pd.DataFrame(dic_frequencia)
df.to_excel("frequencia.xlsx", index=False)