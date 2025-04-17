import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site
url = "https://books.toscrape.com/"

# Requisição HTTP
response = requests.get(url)

# Criar um objeto BeautifulSoup para analisar HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Criar uma lista
books_data = []

# Inspecionar o site e descobrir a tag(article) e seu nome(product_pod)
books = soup.find_all('article', class_= 'product_pod')

for book in books:
    title = book.h3.a.attrs['title']
    price = book.find('p', class_= 'price_color')
    books_data.append([title, price])

df =pd.DataFrame(books_data, columns=['Título', 'Preço'])

df.to_excel('livros.xlsx', index=False)

print("Dados salvos!")