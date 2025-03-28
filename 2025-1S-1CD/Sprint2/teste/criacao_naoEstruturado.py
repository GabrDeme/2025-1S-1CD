import pandas as pd

dados_csv = {
    "Nome": ["Gabriel", "Carlos", "Jéssica"],
    "Idade": [17, 38, 25],
    "Cidade": ["São Paulo", "Ribeirão Pires", "São Paulo"]
}

df_csv = pd.DataFrame(dados_csv)

# salvando em cvs
df_csv.to_csv("dadosNao.csv")