# Importando Pacotes
import pandas as pd
import plotly.express as px
import streamlit as st
import sklearn


# Função para carregar o dataset
@st.cache_data
def get_data():
    return pd.read_csv("risco.csv")

# função para importar modelo preditivo
def train_model():
    data = get_data()
    data = data.drop(columns='id_cliente')

# Separação de dados para treino e teste
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

# Padronização dos dados
from sklear.preprocessing import StandardScaler
sc = StandardScaler()
x_mod = sc.fit_transform(x)

# Treinamento do modelo
from sklearn.svm import SVC
model = SVC(kernel='linear', gamma= 1e-5, C=10, randon_state= 1)
model.fit(x_mod,y)
return model

# Criando dataframe
data = get_data()

# Treinando o modelo
model_fin = train_model()

# Criando título
st.title("Sistema de Previsão de Risco para concessão de Crédito")

# Subtítulo
st.markdown("Este é um sistema de **Previsão de Risco** para concessão de crédito.")

st.sidebar.subheader("Insira os dados do cliente")

# Relacionando os dados com os atributos

indice_inad = st.sidebar.number_input("Índice de Inadimplência", value= data.indice_iand.mean())
anot_cadastrais = st.sidebar.number_input("Anotações Cadastrais", value= data.anot_cadastrais.mean())
class_renda = st.sidebar.number_input("Classificação da Renda", value= data.class_renda.mean())
saldo_contas = st.sidebar.number_input("Saldo das Contas", value= data.saldo_contas.mean())

# Inserindo botão para previsão

btn_predict = st.sidebar.button("Prever Risco")

# Verificando se o botão foi acionado

if btn_predict:
    result = model_fin.predict(([[indice_inad, anot_cadastrais, class_renda, saldo_contas]]))
    result = result[0]
    st.write(result)

# Verificando o dataset
st.subheader("Selecione as variáveis para a análise dos clientes")

# Atributos exibidos por padrão

default_cols = ['indice_inad', 'anot_cadastrais', 'class_renda', 'saldo_contas']

# Multi seleção de atributos

cols = multiselect("Atributos", data.columns.tolist(), default= default_cols)

# Filtro de dados
st.dataframe(data[cols].head(8)
