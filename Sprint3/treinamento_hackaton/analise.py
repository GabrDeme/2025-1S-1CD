import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dashboard Financeiro da Empresa", page_icon="🛒", layout="wide")

# Carregar os dados
df_despesas = pd.read_excel("despesas_limpo.xlsx")
df_orcamento = pd.read_excel("orcamentos_limpo.xlsx")

def SideBar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Bases de Dados",
            options=["Despesas", "Orçamentos"],
            icons=["💸", "💰"],
            default_index=0
        )

    if selecionado == "Despesas":
        Home()
        Despesas()
    elif selecionado == "Orçamentos":
        Home()
        Orcamentos()

""" FILTROS """
st.sidebar.header("🧾 Filtros")

# Filtro por setor
setores = st.sidebar.multiselect(
    "🛠 Setor",
    options=df_despesas["setor"].unique(),
    default=df_despesas["setor"].unique(),
    key="setor"
)

tipos_despesa = st.sidebar.multiselect(
    "💵 Tipo de Despesa",
    options=df_despesas["tipo"].unique(),
    default=df_despesas["tipo"].unique(),
    key="tipo"
)

df_despesas_filtrado = df_despesas.query("setor in @setores and tipo in @tipos_despesa")

def Home():
    st.title("📊 Visão Financeira da Empresa")

    total_despesas = df_despesas_filtrado["valor"].sum()
    media_despesas = total_despesas/24

    df_despesas_filtrado['data'] = pd.to_datetime(df_despesas_filtrado['data'])

    data_atual = pd.to_datetime("today")
    inicio_trimestre = data_atual - pd.DateOffset(months=3)
    
    df_ultimo_trimestre = df_despesas_filtrado[df_despesas_filtrado['data'] >= inicio_trimestre]

    total_ultimo_trimestre = df_ultimo_trimestre["valor"].sum()
    media_ultimo_trimestre = total_ultimo_trimestre/3

    total1, total2, total3, total4 = st.columns(4)
    with total1:
        st.metric("🔢 Total de Despesas", value=f"R${total_despesas:,.2f}")
    with total2:
        st.metric("📈 Média de Despesa", value=f"R${media_despesas:,.2f}")
    with total3:
        st.metric("📅 Total de Despesas no Último Trimestre", value=f"R${total_ultimo_trimestre:,.2f}")
    with total4:
        st.metric("📈 Média de Despesa no Último Trimestre por Mês", value=f"R${media_ultimo_trimestre:,.2f}")

    st.markdown("---")

##############################################################################################################################################################################

def Despesas():
    st.title("📉 Análise de Despesas por Setor")

    fig_barras = px.bar(
        df_despesas_filtrado,
        x="setor",
        y="valor",
        color="setor",
        title="📊 Despesas por Setor",
        labels={"valor": "Total das Despesas", "setor": "Setor"}
    )

    st.plotly_chart(fig_barras, use_container_width=True)

##############################################################################################################################################################################

def Orcamentos():
    st.title("💰 Análise de Orçamento vs. Realizado")

    df_orcamento_filtrado = df_orcamento.query("setor in @setores")

    fig_barras_orcamento = px.bar(
        df_orcamento_filtrado,
        x="setor",
        y=["valor_previsto", "valor_realizado"],
        barmode="group",
        title="📊 Comparativo entre Orçamento Previsto e Realizado por Setor",
        labels={"valor_previsto": "Valor Previsto", "valor_realizado": "Valor Realizado"}
    )

    st.plotly_chart(fig_barras_orcamento, use_container_width=True)

SideBar()
