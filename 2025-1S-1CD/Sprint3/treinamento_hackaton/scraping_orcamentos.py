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

wait = WebDriverWait(driver, 10)

orçamento_button = wait.until(
    ec.element_to_be_clickable((By.XPATH, "//button[text()='Orçamentos']"))
)

while True:
    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, "tr"))
        )
    except TimeoutException:
        print("Tempo acabou!")

    financeiro = driver.find_elements((By.CSS_SELECTOR, "tr"))

    for f in financeiro:
        try:
            data = f.find_element(By.CLASS_NAME, "td_setor").text.strip()
            data = f.find_element(By.CLASS_NAME, "td_mes").text.strip()
            data = f.find_element(By.CLASS_NAME, "td_ano").text.strip()
            data = f.find_element(By.CLASS_NAME, "td_valor_previsto").text.strip()
            data = f.find_element(By.CLASS_NAME, "td_valor_realizado").text.strip()
        except Exception as e:
            print("Erro ", e)
    break
driver.quit()

df = pd.DataFrame(orcamento)
df.to_excel("orcamento.xlsx", index=False)