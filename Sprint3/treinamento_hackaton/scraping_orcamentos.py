from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

chrome_driver = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=service, options=options)

url = "https://masander.github.io/AlimenticiaLTDA-financeiro/"
driver.get(url)
time.sleep(5)

orcamento = {"setor": [], "mes": [], "ano": [], "valor_previsto": [], "valor_realizado": [], }

try:
    botao_orcamento = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, "//button[contains(text())='Orçamentos']"))
    )
    if botao_orcamento:
        driver.execute_script("arguments[0].click();", botao_orcamento)
        time.sleep(5)
except Exception:
    print("Error")
    
while True:
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//tr[contains(@style, \"border-bottom: 1px solid rgb(221, 221, 221)\")]"))
        )
    except TimeoutException:
        print("Tempo acabou!")

    financeiro = driver.find_elements(By.XPATH, "//tr[contains(@style, \"border-bottom: 1px solid rgb(221, 221, 221)\")]")

    for f in financeiro:
        try:
            setor = f.find_element(By.CLASS_NAME, "td_setor").text.strip()
            mes = f.find_element(By.CLASS_NAME, "td_mes").text.strip()
            ano = f.find_element(By.CLASS_NAME, "td_ano").text.strip()
            valor_previsto = f.find_element(By.CLASS_NAME, "td_valor_previsto").text.strip()
            valor_realizado = f.find_element(By.CLASS_NAME, "td_valor_realizado").text.strip()

            orcamento["setor"].append(setor)
            orcamento["mes"].append(mes)
            orcamento["ano"].append(ano)
            orcamento["valor_previsto"].append(valor_previsto)
            orcamento["valor_realizado"].append(valor_realizado)

            print(f"{setor} - {mes} - {ano} - {valor_previsto} - {valor_realizado}")
        except Exception as e:
            print("Erro ", e)
    break
driver.quit()

df = pd.DataFrame(orcamento)
df.to_excel("orcamento.xlsx", index=False)