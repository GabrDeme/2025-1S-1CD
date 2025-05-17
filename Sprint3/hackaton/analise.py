import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Dashboard Alimentícia Ltda - RH", page_icon="📊", layout="wide")

# Carregar dados
df = pd.read_excel("funcionarios_limpo.xlsx")

# --- Filtros Globais ---
st.sidebar.header("📌 Filtros Globais")

turnos = st.sidebar.multiselect(
    "🔁 Selecione o Turno",
    options=df["Turno"].unique(),
    default=df["Turno"].unique(),
)

cargos = st.sidebar.multiselect(
    "👷 Selecione o Cargo",
    options=df["Cargo"].unique(),
    default=df["Cargo"].unique(),
)

setores = st.sidebar.multiselect(
    "🏢 Selecione o Setor",
    options=df["Setor"].unique(),
    default=df["Setor"].unique(),
)

# Aplicar filtros ao DataFrame
df_filtrado = df.query("Turno in @turnos and Cargo in @cargos and Setor in @setores")

# Menu lateral
def SideBar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title="Bases de Dados",
            options=["Horas Extras", "Faltas"],
            icons=["➕", "🙋"],
            default_index=0
        )

    if selecionado == "Horas Extras":
        Horas_Extras()
        Setor()
    elif selecionado == "Faltas":
        Faltas()
        Colaboradores()

# Página de Horas Extras
def Horas_Extras():
    st.title("📊 Análise de Horas Extras por Turno")

    st.subheader("Horas Extras por Cargo e Turno")
    agrupado_cargo = df_filtrado.groupby(["Cargo", "Turno"])["Horas_extras"].sum().reset_index()

    fig_extra_turno = px.bar(
        agrupado_cargo,
        x="Turno",
        y="Horas_extras",
        color="Cargo",
        barmode="group",
        title="Horas Extras por Cargo e Turno",
        labels={"Horas_extras": "Horas Extras Totais"},
        height=500
    )
    st.plotly_chart(fig_extra_turno, use_container_width=True)

    st.subheader("Horas Extras por Setor e Turno")
    agrupado_setor = df_filtrado.groupby(["Setor", "Turno"])["Horas_extras"].sum().reset_index()

    fig_extras_setor = px.bar(
        agrupado_setor,
        x="Turno",
        y="Horas_extras",
        color="Setor",
        barmode="group",
        title="Horas Extras por Setor e Turno",
        labels={"Horas_extras": "Horas Extras Totais"},
        height=500
    )
    st.plotly_chart(fig_extras_setor, use_container_width=True)

# Página de análise por setor
def Setor():
    st.title("📉 Análise de Horas Extras por Setor")

    setor_hora = df_filtrado.groupby('Setor', as_index=False)['Horas_extras'].sum()
    
    fig_extras_pie = px.pie(
        setor_hora,
        names='Setor',
        values='Horas_extras',
        title='Distribuição de Horas Extras por Setor',
        hole=0,
    )

    st.plotly_chart(fig_extras_pie, use_container_width=True)

# Página de Faltas (dados simulados)
def Faltas():
    faltas = {
        'id_func': [8, 8, 8, 8, 8, 13, 13, 13, 13, 13, 25, 25, 25, 25, 25, 25, 40, 40, 40, 40, 40, 40, 84, 84, 84, 84, 84, 84, 84],
        'turno': ['tarde', 'tarde', 'tarde', 'tarde', 'tarde', 'manhã', 'manhã', 'manhã', 'manhã', 'manhã',
                  'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite',
                  'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite', 'noite'],
        'data_falta': ['29-04-2025', '24-04-2025', '22-04-2025', '21-04-2025', '12-04-2025',
                       '03-05-2025', '02-05-2025', '22-04-2025', '11-04-2025', '08-04-2025',
                       '30-04-2025', '17-04-2025', '16-04-2025', '14-04-2025', '12-04-2025', '09-04-2025',
                       '01-05-2025', '29-04-2025', '28-04-2025', '25-04-2025', '17-04-2025', '14-04-2025',
                       '04-05-2025', '25-04-2025', '24-04-2025', '18-04-2025', '13-04-2025', '12-04-2025', '11-04-2025']
    }
    df_faltas = pd.DataFrame(faltas)

    faltas_por_func = df_faltas.groupby('id_func').size().reset_index(name='Qtd_faltas')
    top5 = faltas_por_func.sort_values(by='Qtd_faltas', ascending=False).head(5)

    turnos_mais_frequentes = df_faltas.groupby(['id_func', 'turno']).size().reset_index(name='count')
    turno_predominante = turnos_mais_frequentes.sort_values('count', ascending=False).drop_duplicates('id_func')
    top5 = top5.merge(turno_predominante[['id_func', 'turno']], on='id_func')

    fig_faltas_pessoas = px.bar(
        top5,
        x='id_func',
        y='Qtd_faltas',
        color='turno',
        text='Qtd_faltas',
        title='Colaboradores com Mais Faltas em 2025',
        labels={'id_func': 'ID Funcionário', 'Qtd_faltas': 'Quantidade de Faltas', 'turno': 'Turno'},
        height=500
    )

    fig_faltas_pessoas.update_traces(textposition='outside')
    fig_faltas_pessoas.update_layout(xaxis=dict(type='category'))

    st.plotly_chart(fig_faltas_pessoas, use_container_width=True)

# Página de análise de faltas por turno
def Colaboradores():
    st.title("💰 Análise de Faltas por Turno")

    faltas_por_turno = df_filtrado.groupby('Turno')['Faltou'].sum().reset_index()
    faltas_por_turno = faltas_por_turno.sort_values(by='Faltou', ascending=False)

    fig_faltas_turno = px.bar(
        faltas_por_turno,
        x='Turno',
        y='Faltou',
        title='Total de Faltas por Turno',
        labels={'Faltou': 'Quantidade de Faltas'},
        color='Turno',
        text='Faltou',
        height=500
    )

    fig_faltas_turno.update_traces(textposition='outside')
    fig_faltas_turno.update_layout(yaxis_title='Quantidade de Faltas', xaxis_title='Turno', showlegend=False)

    st.plotly_chart(fig_faltas_turno, use_container_width=True)

# Rodar app
SideBar()
