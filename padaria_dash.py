import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
st.set_page_config(page_title="pao de deus", page_icon="🦑", layout="wide")
st.title("Bem vindo a padaria:  **PAO DE DEUS** ")
nome = st.text_input("Digite seu mome")
st.markdown("_"*40)
st.write(nome)
st.markdown("_"*40)


df_produtos = pd.DataFrame({
    "Produto": [
        "Pão Francês", "Pão de Queijo", "Croissant",
        "Bolo de Chocolate", "Café Expresso",
        "Cappuccino", "Sonho", "Pão Doce",
        "Rosquinha", "Baguete"
    ],
    "Categoria": [
        "Pães", "Salgados", "Folhados", "Bolos",
        "Bebidas", "Bebidas", "Doces", "Pães",
        "Doces", "Pães"
    ],
    "Preço": [
        1.00, 3.50, 7.00, 12.00, 5.00,
        8.00, 6.00, 4.00, 3.00, 9.00
    ],
    "Estoque": [
        150, 100, 45, 20, 200,
        100, 50, 80, 90, 35
    ]
})

df_vendas = pd.DataFrame({
    "Produto": [
        "Pão Francês", "Pão de Queijo", "Croissant",
        "Bolo de Chocolate", "Café Expresso",
        "Cappuccino", "Sonho", "Pão Doce",
        "Rosquinha", "Baguete"
    ],
    "Quantidade Vendida": [
        350, 220, 95, 75, 180,
        110, 85, 140, 120, 65
    ]
})

df_vendas = df_vendas.merge(
    df_produtos[["Produto", "Preço"]],
    on="Produto",
    how="left"
)

df_vendas["Total"] = (
    df_vendas["Quantidade Vendida"] * df_vendas["Preço"]
)



st.dataframe(df_vendas)
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro numero", value=0.0, step=1.0)
with col2:
    num2 = st.number_input("Segundo numero", value=0.0, step=1.0)
    
operacao = st.selectbox(
    "ESCOLHA OPERACAO",
    ["Adição (+)", "Subtração (-)", "Multiplicação (x)", "Divisao (/)"],
    
)




resultado = None

if st.button("Calcular", type="primary"):
    
    if operacao == "Adição (+)":
        resultado = num1 + num2
    if operacao == "Subtração (-)":
        resultado = num1 - num2
    if operacao == "Multiplicação (x)":
        resultado = num1 * num2
    if operacao == "Divisao (/)":
        resultado = num1 / num2

if resultado is not None:
    st.write(resultado)    