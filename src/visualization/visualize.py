import pandas as pd
import streamlit as st
import scipy as sci
import plotly.express as px
import plotly.graph_objects as go

def create_histogram(df, column, color):
    # Verificar se a coluna existe no DataFrame
    if column not in df.columns:
        raise ValueError(f"A coluna {column} não existe no DataFrame.")

    # Verificar se a coluna é numérica
    if df[column].dtype not in ['float64', 'int64']:
        raise ValueError(f"A coluna {column} não é numérica.")

    # Criar o histograma para a coluna
    hist = go.Histogram(
        x=df[column].values,
        histnorm='percent',
        name=f'Histograma de {column}',
        marker={'color': color}
    )

    # Calcular a média da coluna e criar uma linha indicadora
    mean_value = df[column].mean()
    line = go.Scatter(
        x=[mean_value, mean_value],
        y=[0, 3], 
        mode='lines',
        name=f'Média de {column}',
        line={'color': '#FF8360', 'dash': 'dash'}
    )
    
    # Criar a figura e adicionar os elementos gráficos
    fig = go.Figure(data=[hist, line])
    fig.update_layout(
        title=f'Distribuição e Média da Coluna {column}',
        xaxis_title=column,
        yaxis_title='Percentual',
        barmode='overlay'
    )
    
    return fig


def plot_price_by_model_year(df, min_year=1908):
    """
    Função para criar um gráfico de bolhas mostrando a distribuição do preço por ano do modelo de veículos.
    
    Args:
    df (pd.DataFrame): DataFrame contendo as colunas 'model_year' e 'price'.
    min_year (int): Ano mínimo para filtrar os veículos.
    
    Returns:
    None, exibe um gráfico de bolhas.
    """
    # Filtrar o DataFrame para anos do modelo maiores que min_year
    df_filtered = df[df['model_year'] > min_year]

    # Criar o gráfico de bolhas
    fig = px.scatter(df_filtered, x='model_year', y='price',
                     title='Distribuição do Preço por Ano do Modelo',
                     labels={'model_year': 'Ano do Modelo', 'price': 'Preço'},
                     size='price',  # O tamanho das bolhas representa o preço
                     color='model_year',  # Cor por ano para visualização da tendência ao longo do tempo
                     color_continuous_scale=px.colors.sequential.Viridis,
                     template='plotly_white')

    fig.update_layout(
        xaxis_title='Ano do Modelo',
        yaxis_title='Preço',
        title={
            'text': "Relação entre Preço e Ano do Modelo dos Veículos",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    fig.update_layout(margin=dict(t=60))

    return fig