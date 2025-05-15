import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Configurações iniciais
st.set_page_config(page_title="Dashboard de Vendas", page_icon="🛒", layout="wide")

# Carregar os dados
df = pd.read_excel("Vendas.xlsx")

""" FILTROS """
# Sidebar
st.sidebar.header("🧾 Selecione os Filtros")

# Filtro por loja
lojas = st.sidebar.multiselect( # Vários podem ser selecionados
    "🏬 Lojas", # Label: Nome do filtro
    options=df["ID Loja"].unique(), # Sem o 'unique()' todas as lojas seriam selecionadas
    default=df["ID Loja"].unique(), # Por padrão todos estarão selecionados
    key="loja" # Chave para esse filtro
) 

produtos = st.sidebar.multiselect(
    "📦 Produtos",
    options=df['Produto'].unique(),
    default=df['Produto'].unique(),
    key="produto"
)

# Filtrar o Dataframe de acordo com as opções
df_selecao = df.query("`ID Loja` in @lojas and Produto in @produtos") # O '`' pe utilizado para mencionar a coluna e o '@' para mencionar os filtros

# Gráficos e na função da página
def Home():
    st.title("📊 Faturamento das Lojas")

    total_vendas = df["Quantidade"].sum()
    media = df["Quantidade"].mean()
    mediana = df["Quantidade"].median()

    total1, total2, total3 = st.columns(3)
    with total1:
        # Apresentando inidacadores rápidos
        st.metric("🔢 Total Vendido", value=int(total_vendas)) # Esse 'metric' é o tal do apresentador
    with total2:
        st.metric("📈 Média por Produto", value=media)
    with total3:
        st.metric("📊 Mediana", value=int(mediana))

    st.markdown("---")

def Graficos():
    # Gráfico de barras, mostrando a quantdade de produtos por loja
    fig_barras = px.bar(
        df_selecao,
        x="Produto",
        y="Quantidade",
        color="ID Loja",
        barmode="group", # Funciona junto com o 'color' para visualização de cores
        title="📦 Quantidade de Produtos Vendidos por Loja"
    )
    
    # Gráfico de linha, com o total de vendas por loja
    fig_linha = px.line(
        df.groupby(["ID Loja"]).sum(numeric_only=True).reset_index(),
        x="ID Loja",
        y="Quantidade",
        title="📉 Total de Vendas por Loja"
    )

    # Disposição dos gráficos ou COLUNA ou Linha
    graf1, graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(fig_barras, use_container_width=True) # 'plotly_chart' serve para mostrar o gráfico; 'use_container_width' se refere a largura do gráfico
    with graf2:
        st.plotly_chart(fig_linha, use_container_width=True)

def SideBar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Menu",
            options=["Home", "Gráficos"],
            icons=["house", "bar-chart"],
            default_index=0
        )

    if selecionado == "Home":
        Home()
        Graficos()
    elif selecionado == "Gráficos":
        Graficos()

SideBar()
