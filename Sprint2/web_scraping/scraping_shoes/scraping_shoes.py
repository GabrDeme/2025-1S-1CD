from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

chrome_driver_path = "C:\\Program Files\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.netshoes.com.br/busca?nsCat=Natural&q=tenis%20masculino%20adidas%20preto&genero=masculino&genero=menino&tipo-de-produto=tenis&tipo-de-produto=tenis-performance&marca=adidas"
driver.get(url)
time.sleep(5)

products = {"tenis": [], "preco": []}
page = 1

while True:
    print(f"\nColetando os dados da página {page}...")

    # Espera os produtos carregarem
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card__description--name"))
    )

    names = driver.find_elements(By.CLASS_NAME, "card__description--name")
    price_elements = driver.find_elements(By.XPATH, '//span[@data-price="price"]')

    # Aguarda que todos os preços carreguem com valor diferente de “Confira” ou vazio
    print("Aguardando todos os preços ficarem disponíveis...")
    timeout = 20
    interval = 0
    while interval < timeout:
        all_loaded = True
        for elem in price_elements:
            text = elem.text.strip()
            if text == "" or text.lower() == "confira":
                all_loaded = False
                break
        if all_loaded:
            break
        time.sleep(1)
        interval += 1
        price_elements = driver.find_elements(By.XPATH, '//span[@data-price="price"]')  # atualiza

    print(f"Produtos encontrados: {len(names)} | Preços encontrados: {len(price_elements)}")

    for name, price in zip(names, price_elements):
        products["tenis"].append(name.text.strip())
        products["preco"].append(price.text.strip())
        print(f"{name.text.strip()}: {price.text.strip()}")

    try:
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pagination__next"))
        )
        if next_button:
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", next_button)
            print(f"Indo para a página {page + 1}")
            page += 1
            time.sleep(5)
        else:
            print("Última página.")
            break
    except Exception as e:
        print("Erro ao mudar de página:", e)
        break

driver.quit()

df = pd.DataFrame(products)
df.to_excel("tenis.xlsx", index=False)

print(f"\nExcel com dados dos tênis criado com sucesso! {len(df)} produtos capturados.")
