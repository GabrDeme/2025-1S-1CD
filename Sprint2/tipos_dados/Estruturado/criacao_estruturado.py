# pip install pandas
# pip install openpyxl

import pandas as pd

# criando uma base de dados
dados_planilha1 = {
    "Nome": ["Gabriel", "Carlos", "Jéssica"],
    "Idade": [17, 38, 25],
    "Cidade": ["São Paulo", "Ribeirão Pires", "São Paulo"]
}

# criando um dataframe
df_planilha1 = pd.DataFrame(dados_planilha1)

print(df_planilha1)

# salvar no excel
with pd.ExcelWriter("dadosEstruturados.xlsx") as writer:
    df_planilha1.to_excel(writer, sheet_name="Planilha1", index=False)