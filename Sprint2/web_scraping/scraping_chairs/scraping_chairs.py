# Módulo de controle do navegador
from selenium import webdriver

# Localizador de elementos
from selenium.webdriver.common.by import By

# Serviço de configuração do caminho do executável chromedriver
from selenium.webdriver.chrome.service import Service

# Classe que permite executar ações avançadas(mover do mouse, clique/arrasta e etc)
from selenium.webdriver.common.action_chains import ActionChains

# Classe que espera a condição ser satisfeita
from selenium.webdriver.support.ui import WebDriverWait

# Condições esperadas com WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import pandas as pd

# Funções sobre o tempo
import time

# Tratamento de exceção
from selenium.common.exceptions import TimeoutException

# Caminho do Webdriver
chrome_driver_path = "C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Configurações do Webdriver
service = Service(chrome_driver_path) # Navegador controlado pelo Selenium
options = webdriver.ChromeOptions() # Configurações do navegador
""" options.add_argument("--headless") """ # Executa o navegador sem abrir uma interface gráfica
options.add_argument("--disable-gpu") # Evita possíveis erros gráficos
options.add_argument("--window-size=1920,1080") # Resolução fixa

# Inicialização do Webdriver
driver = webdriver.Chrome(service=service, options=options)

# URL inicial
url_base = "https://www.kabum.com.br/espaco-gamer/cadeiras-gamer"
driver.get(url_base)
time.sleep(5) # Espera 5 segundos após ação

# Dicionário que armazena marcas e preços
dic_produtos = {"marca": [], "preço": []}

# Início na página 1
pagina = 1

while True:
    print(f"\n Coletando os dados da página {pagina}...")

    try:
        WebDriverWait(driver, 10).until( # Espera de 10 segundos, espera que essa condição seja verdadeira
            ec.presence_of_all_elements_located((By.CLASS_NAME, "productCard")) # Verifica se todos os elementos estão acessíveis, indica qual será a classe vasculhada
        )
    except TimeoutException:
        print("Tempo de espera excedido!")
    
    produtos = driver.find_elements(By.CLASS_NAME, "productCard")

    for produto in produtos:
        try:
            nome = produto.find_element(By.CLASS_NAME, "nameCard").text.strip()
            preco = produto.find_element(By.CLASS_NAME, "priceCard").text.strip()

            print(f"{nome}: {preco}")

            dic_produtos["marca"].append(nome)
            dic_produtos["preço"].append(preco)
        except Exception as e:
            print("Erro ao coletar dados: ", e)
    
    try:
        # Encontra o elemento de ir para a próxima página, vulgo setinha
        botao_proximo = WebDriverWait(driver, 5).until(
            ec.element_to_be_clickable((By.CLASS_NAME, "nextLink"))
        )

        if botao_proximo:
            driver.execute_script("arguments[0].scrollIntoView();", botao_proximo)
            time.sleep(1)

            # Clique no botão
            driver.execute_script("arguments[0].click();", botao_proximo)
            print(f"Indo para a página {pagina} ")
            pagina += 1
            time.sleep(5)

        else:
            print("Você chegou na última página!")
            break



    except Exception as e:
        print("Erro ao tentar avançar para a próxima página: ", e)
        break
# Deleta o navegador
driver.quit()

df = pd.DataFrame(dic_produtos)
df.to_excel("cadeiras.xlsx", index=False)

print(f"Arquivo 'cadeiras' salvo com sucesso! {len(df)} produtos capturados")