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
url = "https://www.kabum.com.br/tablets-ipads-e-e-readers"
driver.get(url)
time.sleep(5)

tablets = {"item": [], "preco": []}

page = 1

while True: 
    print(f"\n Estamos na página {page}")

    try:
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "productCard"))
        )
    except TimeoutException:
        print("Tempo de espera excedido!")

    products = driver.find_elements(By.CLASS_NAME, "productCard")
    
    for product in products:
        try:
            item = product.find_element(By.CLASS_NAME, "nameCard").text.strip()
            price = product.find_element(By.CLASS_NAME, "priceCard").text.strip()

            print(f"{item}: {price}")

            tablets["item"].append(item)
            tablets["preco"].append(price)
        except Exception as e:
            print("Erro ao coletar dados: ", e)
    try:
        next_button = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "nextLink"))
        )

        if next_button:
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(1)

            driver.execute_script("arguments[0].click();", next_button)
            page +=1
            print(f"Indo para a página {page}")
            time.sleep(5)

        else:
            print("Você chegou na última página!")
    except Exception as e:
        print("Erro ao tentar avançar para a próxima página: ", e)
        break
driver.quit()

df = pd.DataFrame(tablets)
df.to_excel("tablets.xlsx", index=False)

print(f"Arquivo 'tablets' salvo com sucesso! {len(df)} produtos capturados")
