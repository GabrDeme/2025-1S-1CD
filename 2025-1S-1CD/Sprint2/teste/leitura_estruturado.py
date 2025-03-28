import pandas as pd

df_excel = pd.read_excel("dadosEstruturados.xlsx", sheet_name=["Planilha1"])

df_aba1 = df_excel["Planilha1"]
# df_aba2 = df_excel["Planilha2"]

print(df_excel)