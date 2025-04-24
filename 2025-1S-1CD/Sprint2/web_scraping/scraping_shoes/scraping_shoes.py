from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time
from selenium.common.exceptions import TimeoutException

chrome_driver_path = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path) 
options = webdriver.ChromeOptions() 
options.add_argument("--disable-gpu") 
options.add_argument("--window-size=1920,1080") 

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.netshoes.com.br/busca?nsCat=Natural&q=tenis%20masculino%20adidas%20preto&genero=masculino&genero=menino&tipo-de-produto=tenis&tipo-de-produto=tenis-performance&marca=adidas"
driver.get(url)
time.sleep(15) 

products = {"tenis": [], "preco": []}

page = 1

while True:
    print(f"\n Coletando os dados da página {page}...")

    try:
        WebDriverWait(driver, 60).until( 
            ec.presence_of_all_elements_located((By.CLASS_NAME, "card__description"))
        )
    except TimeoutException:
        print("Tempo de espera excedido!")
    
    prods = driver.find_elements(By.CLASS_NAME, "card__description")

    for prod in prods:
        try:
            shoe = prod.find_element(By.CLASS_NAME, "card__description--name").text.strip()
            price = prod.find_element(By.XPATH, '//span[@data-price="price"]').text


            print(f"{shoe}: {price}")

            products["tenis"].append(shoe)
            products["preco"].append(price)
        except Exception as e:
            print("Erro ao coletar dados: ", e)
    
    try:
        next_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "pagination__next"))
        )

        if next_button:
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(1)

            driver.execute_script("arguments[0].click();", next_button)
            print(f"Indo para a página {page} ")
            page += 1
            time.sleep(5)

        else:
            print("Você chegou na última página!")
            break



    except Exception as e:
        print("Erro ao tentar avançar para a próxima página: ", e)
        break
driver.quit()

df = pd.DataFrame(products)
df.to_excel("tenis.xlsx", index=False)

print(f"Excel com dados dos tenis da Adidas da empresa Netshoes criado com sucesso! {len(df)} produtos capturados")