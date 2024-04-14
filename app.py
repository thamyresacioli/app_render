import streamlit as st
import src.visualization.visualize as viz
from src.dataset import make_dataset
from src.dataset.make_dataset import read_and_process_data
import pandas as pd 

st.header("Aplicativo")


df = read_and_process_data('vehicles_us.csv')
hist_checkbox = st.checkbox('Criar histograma de preços')
scatter_checkbox = st.checkbox('Distribuição de preços de carro por ano')


fig = viz.plot_price_by_model_year(df)

if hist_checkbox:
    st.write('Criando um histograma dos preços de anúncios de vendas de carros')

    fig_2 = viz.create_histogram(df, 'price', '#45CB85')
    st.plotly_chart(fig_2, use_container_width=True)

if scatter_checkbox:
    st.write('Distribuição dos preços por ano do carro')

    fig = viz.plot_price_by_model_year(df, 1980)
    st.plotly_chart(fig, use_container_width=True)
