# Passo 1: Instalar -> pip install streamlit pandas ploty (casao não esteja instalado)
# Este codigo deve ser executado no terminal com: streamlit run nome_codigo.py 
    # Ou python -m streamlit run nome_codigo.py
# criar uma conta no GitHub para hospedar os dados 
# criar um novo arquivo requirements.txt e coloca nele streamlit pandas plotly
# Cria um diretotior no GitHub e coloca os arquivos em codigo.py requirements.txt e vendas.csv
    # https://github.com/fabioonajart/Sistema_Vendas_e_Gest-o_Online_curso/upload
# Fazer Deploy -> é o ato de publicar seu sistema para que outras pessoas possam acessá-lo pelo navegador
    # Acesse o Streamlit Cloud -> faz login com GitHun
    # Crie um novo app
    # Publique o sistema
    # Compartilhe o link

import streamlit as st
import pandas as pd
import plotly.express as px   

# Cadastra a base de ventas

tabela_vendas = pd.read_csv('vendas.csv')

st.write('# Sistema de vendas')

# Seção cadastrar vendas
st.sidebar.write('## Cadastrar Vendas') # sideber -> coloca tudo em uma barra na esquerda da pagina
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendedor', ['Ana', 'Bruno', 'Carla'])
produto = st.sidebar.selectbox('Produto', ['Notebook', 'Celular', 'Fone'])
quantidade = st.sidebar.number_input('quantidade', step = 1) # Usa o step = 1 para numero selecionado seja inteiro
valor = st.sidebar.number_input('Valor')
botao_cadastrar = st.sidebar.button('Cadastrar vendas')

if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas) # tamanho da tabela)
    tabela_vendas.loc[ultima_linha] = nova_venda 
    tabela_vendas.to_csv('vendas.csv', index = False)
    print(nova_venda)
    st.success('Vendas cadastradas')

# Seção de visualizar vendas cadastradas
st.write('## Vendas Cadastradas')
st.dataframe(tabela_vendas) # dateframe são tabelas do pandas

# Seção Dashboard
st.write('## Dashboard')

# Calculo do faturamento somando os valores da colula valor da tabela de vendas
faturamento = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R$ {faturamento}') # cria um campo de faturamento a baixo de Dashboard

# Grafico de barra
grafico1 = px.bar(tabela_vendas, x = 'vendedor', y = 'valor', color = 'produto') # plota o grafico na pagina
st.plotly_chart(grafico1)
# grafico1.show() plota o grafico no terminal

# Grafico de pizza
grafico2 = px.pie(tabela_vendas, names = 'produto', values = 'valor', hole = 0.5)
st.plotly_chart(grafico2)