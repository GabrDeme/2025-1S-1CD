
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as ec  
import time
from selenium.common.exceptions import TimeoutException

chrome_driver_path = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.imdb.com/chart/top/"

driver.get(url)
time.sleep(5)

dic_filmes = {"nome": [], "faixa_etaria":[], "ano":[]}

def safe_find_text(element, selector):
    try:
        return element.find_element(By.CSS_SELECTOR, selector).text
    except Exception:
        return "Desconhecido"

while True:

    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "ipc-metadata-list-summary-item"))
        )
    except TimeoutException as e:
        print("Tempo:", e)
    
    filmes = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item")

    for filme in filmes:
        try:
            nome = filme.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text.strip()
            ano = filme.find_element(By.CSS_SELECTOR, "span.sc-5179a348-7.idrYgr.cli-title-metadata-item").text.strip()
            faixa_etaria = filme.find_element(By.CSS_SELECTOR, "div.sc-5179a348-6.bnnHxo.cli-title-metadata").text.strip()

            print(f"{nome}: {faixa_etaria}: {ano}")

            dic_filmes["nome"].append(nome)
            dic_filmes["faixa_etaria"].append(faixa_etaria)
            dic_filmes["ano"].append(ano)

        except Exception as e:
            print(e)

    break           

driver.quit()

df = pd.DataFrame(dic_filmes)
df.to_excel("filmes.xlsx", index = False)

print(f"Arquivo 'filmes' salvo com sucesso {len(df)}")
