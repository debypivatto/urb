import os 
import pandas as pd
import plotly.express as px
import streamlit as st

df_car_data = pd.read_csv('vehicles.csv')

fig = px.histogram(df_car_data, x="odometer") # criar um histograma
fig.show() # exibindo

fig = px.scatter(df_car_data, x="odometer", y="price") # criar um gráfico de dispersão
fig.show() # exibindo

hist_button = st.button('Criar histograma') # criar um botão
if hist_button: # se o botão for clicado
         # escrever uma mensagem
        st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
# criar um histograma
fig = px.histogram(df_car_data, x="odometer")  # exibir um gráfico Plotly interativo
st.plotly_chart(fig, use_container_width=True)
# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')