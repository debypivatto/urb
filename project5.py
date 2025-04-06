import os 
import pandas as pd
import plotly.express as px
import streamlit as st

df_car_data = pd.read_csv('vehicles.csv') # carregar os dados do arquivo

st.title ('Análise de Dados de Veículos')

fig = px.histogram(df_car_data, x="odometer") # criar um histograma dos carros
fig.show() # exibindo

fig = px.scatter(df_car_data, x="odometer", y="price") # criar um gráfico de dispersão por preco
fig.show() # exibindo

if st.button('Criar histograma'):
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para criar histograma
if st.checkbox('Criar outro histograma (por odômetro)'):
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(df_car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão sempre exibido
st.write("Gráfico de dispersão entre odômetro e preço")
fig = px.scatter(df_car_data, x="odometer", y="price")
st.plotly_chart(fig, use_container_width=True)