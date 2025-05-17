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

botao_proximo = buttons[1]
botao_proximo.click()
time.sleep(5)

dic_funcionarios = {"Id_funcionario": [], "Nome": [], "Sexo": [], "Data_admissao": [], "Cargo": [], "Setor": [], "Turno": [], "Salario": []}


funcionarios = driver.find_elements(By.XPATH, "//table/tbody//tr")

for funcionario in funcionarios:
    try:
        id_funcionario = funcionario.find_element(By.CLASS_NAME, "td_id_funcionario").text.strip()
        nome = funcionario.find_element(By.CLASS_NAME,"td_nome").text.strip()
        sexo = funcionario.find_element(By.CLASS_NAME,"td_sexo").text.strip()
        data_admissao = funcionario.find_element(By.CLASS_NAME,"td_data_admissao").text.strip()
        cargo = funcionario.find_element(By.CLASS_NAME,"td_cargo").text.strip()
        setor = funcionario.find_element(By.CLASS_NAME,"td_setor").text.strip()
        turno = funcionario.find_element(By.CLASS_NAME,"td_turno").text.strip()
        salario = funcionario.find_element(By.CLASS_NAME,"td_salario").text.strip()

        print(f"{id_funcionario} - {nome} - {sexo} - {data_admissao} - {cargo} - {setor} - {turno} - {salario}")

        dic_funcionarios["Id_funcionario"].append(id_funcionario)
        dic_funcionarios["Nome"].append(nome)
        dic_funcionarios["Sexo"].append(sexo)
        dic_funcionarios["Data_admissao"].append(data_admissao)
        dic_funcionarios["Cargo"].append(cargo)
        dic_funcionarios["Setor"].append(setor)
        dic_funcionarios["Turno"].append(turno)
        dic_funcionarios["Salario"].append(salario)
    except Exception as e:
        print("Erro: ", e)

driver.quit()

df = pd.DataFrame(dic_funcionarios)
df.to_excel("funcionarios.xlsx", index=False)