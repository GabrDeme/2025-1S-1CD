import pandas as pd

dados_json = {
    "Nome": ["Gabriel", "Carlos", "Jéssica"],
    "Idade": [17, 38, 25],
    "Cidade": ["São Paulo", "Ribeirão Pires", "São Paulo"]
}

df_json = pd.DataFrame(dados_json)

# salvar em json
df_json.to_json("dadosSemi.json", orient="records", lines=False)