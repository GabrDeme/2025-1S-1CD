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

service = Service(chrome_driver)
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)

url = "https://masander.github.io/AlimenticiaLTDA-financeiro/"
driver.get(url)
time.sleep(5)

despesas = {"data": [], "tipo": [], "setor": [], "valor": [], "fornecedor": []}

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
            data = f.find_element(By.CLASS_NAME, "td_data").text.strip()
            tipo = f.find_element(By.CLASS_NAME, "td_tipo").text.strip()
            setor = f.find_element(By.CLASS_NAME, "td_setor").text.strip()
            valor = f.find_element(By.CLASS_NAME, "td_valor").text.strip()
            fornecedor = f.find_element(By.CLASS_NAME, "td_fornecedor").text.strip()

            despesas["data"].append(data)
            despesas["tipo"].append(tipo)
            despesas["setor"].append(setor )
            despesas["valor"].append(valor)
            despesas["fornecedor"].append(fornecedor)
            print(f"{data} - {tipo} - {setor} - {valor} - {fornecedor}")
        except Exception as e:
            print("Erro ", e)
    break
driver.quit()

df = pd.DataFrame(despesas)
df.to_excel("despesas.xlsx", index=False)


