from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

chrome_driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

servico = Service(chrome_driver_path)
controle = webdriver.ChromeOptions()
controle.add_argument("--disable-gpu")
controle.add_argument("--window-size=1920,1080")

executor = webdriver.Chrome(service=servico, options=controle)

url = "https://www.vivareal.com.br/venda/?transacao=venda&pagina="

executor.get(url)
time.sleep(5)

imoveis = {"rua": [], "valor": [], "valor_condominio": [], "valor_iptu": [], "metragem": [], "quartos": [], "banheiros": [], "vagas": []}
pagina = 1
imovel = 0

while True:
    urlMontada = f'{url}{pagina}'
    print(f"\nColetando dados da página {pagina}")

    try:
        WebDriverWait(executor, 15).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-cy="rp-property-cd"]'))
            # ec.presence_of_all_elements_located((By.CSS_SELECTOR, "a.block.border.border-neutral-90.rounded-1.overflow-hidden.text-neutral-120.group/card.text-start.shadow-bottom-0.duration-1.hover:shadow-bottom-6.transition-shadow.ease-in"))
        )
    except TimeoutException as e:
        print("Demorou muito meu filho", e)

    casinhas = executor.find_elements(By.CSS_SELECTOR, )

    for casinha in casinhas:
        try:
            rua = casinha.find_element(By.CSS_SELECTOR, )
            valor = casinha.find_element(By.CSS_SELECTOR, "")
            valor_iptu = casinha.find_element(By.CSS_SELECTOR, "")
            valor_condominio = casinha.find_element(By.CSS_SELECTOR, "")
            metragem = casinha.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-propertyArea-txt"]')
            quartos = casinha.find_element(By.CSS_SELECTOR, )
            banheiros = casinha.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-bathroomQuantity-txt"]')
            vagas = casinha.find_element(By.CSS_SELECTOR, '[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"]')

            print(f"{rua} : {valor} | {valor_condominio} | {valor_iptu} | {metragem} | {quartos} | {banheiros} | {vagas}")

            imoveis["rua"].append(rua)
            imoveis["valor"].append(valor)
            imoveis["condominio"].append(valor_condominio)
            imoveis["iptu"].append(valor_iptu)
            imoveis["metragem"].append(metragem)
            imoveis["quartos"].append(quartos)
            imoveis["banheiros"].append(banheiros)
            imoveis["vagas"].append(vagas)

        except Exception as e:
            print("Os dados não foram coletados e vc foi avisado ☝️🤓",e)

    if imovel == 100:
        break

executor.quit()

df = pd.DataFrame()
df.to_excel("casinhas.xlsx", index=False)