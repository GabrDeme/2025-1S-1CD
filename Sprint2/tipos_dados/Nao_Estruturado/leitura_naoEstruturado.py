import pandas as pd

df_csv = pd.read_csv("dadosNao.csv")

print(df_csv)
print("-")
print(df_csv["Nome"])