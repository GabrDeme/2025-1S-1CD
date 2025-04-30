from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

# chrome_driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# servico = Service(chrome_driver_path)
controle = webdriver.ChromeOptions()
controle.add_argument("--disable-gpu")
controle.add_argument("--window-size=1920,1080")

# executor = webdriver.Chrome(service=servico, options=controle)
executor = webdriver.Chrome(options=controle)

url = "https://www.vivareal.com.br/venda/?transacao=venda&pagina="

executor.get(url)
time.sleep(5)

imoveis = {"rua": [], "valor": [], "valor_iptu": [], "metragem": [], "quartos": [], "banheiros": [], "vagas": []}
pagina = 1
imovel = 0

def safe_find_text(element, selector):
    try:
        return element.find_element(By.CSS_SELECTOR, selector).text
    except Exception:
        return "Desconhecido"

while imovel <= 100:
    urlMontada = f'{url}{pagina}'
    print(f"\nColetando dados da página {pagina}")

    try:
        WebDriverWait(executor, 15).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-cy="rp-property-cd"]'))
            # ec.presence_of_all_elements_located((By.CSS_SELECTOR, "a.block.border.border-neutral-90.rounded-1.overflow-hidden.text-neutral-120.group/card.text-start.shadow-bottom-0.duration-1.hover:shadow-bottom-6.transition-shadow.ease-in"))
        )
    except TimeoutException as e:
        print("Demorou muito meu filho", e)

    casinhas = executor.find_elements(By.CSS_SELECTOR, '[data-cy="rp-property-cd"]')

    print(f"TAMANHO DA LISTA {len(casinhas)}")

    for casinha in casinhas:
        imovel += 1
        try:
            rua = safe_find_text(casinha, '[data-cy="rp-cardProperty-location-txt"]')
            valor = safe_find_text(casinha, '[data-cy="rp-cardProperty-price-txt"] > p:nth-of-type(1)')
            valor_iptu_cond = safe_find_text(casinha, '[data-cy="rp-cardProperty-price-txt"] > p:nth-of-type(2)')
            metragem = safe_find_text(casinha, '[data-cy="rp-cardProperty-propertyArea-txt"] > h3')
            quartos = safe_find_text(casinha, '[data-cy="rp-cardProperty-bedroomQuantity-txt"] > h3')
            banheiros = safe_find_text(casinha, '[data-cy="rp-cardProperty-bathroomQuantity-txt"] > h3')
            vagas_garagem = safe_find_text(casinha, '[data-cy="rp-cardProperty-parkingSpacesQuantity-txt"] > h3')

        except Exception as e:
            print("Os dados não foram coletados e você foi avisado ☝️🤓", e)

        imoveis["rua"].append(rua)
        imoveis["valor"].append(valor)
        imoveis["valor_iptu"].append(valor_iptu_cond)
        imoveis["metragem"].append(metragem)
        imoveis["quartos"].append(quartos)
        imoveis["banheiros"].append(banheiros)
        imoveis["vagas"].append(vagas_garagem)


        print(f"{rua} - {valor} - {valor_iptu_cond} - {metragem} - {quartos} - {banheiros} - {vagas_garagem}")

    try:

        botao_proximo = WebDriverWait(executor, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="next-page"]'))
            )

        if botao_proximo:
            executor.execute_script("arguments[0].scrollIntoView();", botao_proximo)

            time.sleep(1)

            executor.execute_script("arguments[0].click();", botao_proximo)

            pagina += 1

            print(f"Indo para a página {pagina}")
            time.sleep(5)
    except TimeoutException as e:
        print("Você chegou na última página.", e)
        break
    except Exception as e:
        print("Erro inesperado ao tentar ir para a próxima página:", e)

executor.quit()

df = pd.DataFrame(imoveis)
df.to_excel("casinhas.xlsx", index=False)