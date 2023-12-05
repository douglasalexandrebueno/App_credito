#Importando Pacotes
import pickle
import streamlit as st
import sklearn

#Bibliotecas para manipulação de dados
import pandas as pd
import numpy as np

# Biblioteca utilizada na construção do modelo preditivo
from sklearn.svm import SVC

# biblioteca para imoortação de modelo
from pickle import load

# função para carregar o dataset
@st.cache_data
def get_data():
    return pd.read_csv("clientes.csv")

# função para importar modelo preditivo
def import_model():
    return load(open('modelo_final.pkl','rb'))

def mapear_saida(valor):
    if sexo == "Masculino":
        sexo = 0
    else:
        sexo = 1

    if estado_civil == "Solteiro(a)":
        estado_civil = 0
    else:
        estado_civil = 1

    if historico_credito == "Débitos Pendentes":
        historico_credito = 0
    else:
        historico_credito = 1

    emprestimo = emprestimo / 1000

# Predição

data = get_data()

model = import_model()

prediction = modelo_final.predict( 
        [[sexo, estado_civil, renda, emprestimo, historico_credito]])
     
if prediction == 0:
        pred = 'Rejeitado'
else:
        pred = 'Aprovado'
    return pred


# Essa função é para criação da webpage
def main():

    # Elementos da webpage
    # Nesse Ponto vc deve Personalizar o Sistema com sua Marca
    html_temp = """
    <div style ="background-color:blue;padding:13px">
    <h1 style ="color:white;text-align:center;">SAE</h1>
    <h2 style ="color:white;text-align:center;">Sistema de Aprovação de Empréstimos - by Douglas</h2>
    </div>
    """

    # Função do stramlit que faz o display da webpage
    st.markdown(html_temp, unsafe_allow_html = True)

    # As linhas abaixo criam as caixas na qual o usuário vai entrar com dados da pessoa que quer o empréstimo para fazer a Predição
    sexo = st.selectbox('Sexo',("Masculino","Feminino"))
    estado_civil = st.selectbox('Estado Civil',("Solteiro(a)","Casado(a)"))
    renda = st.number_input("Renda Mensal")
    emprestimo = st.number_input("Valor Total do Empréstimo")
    historico_credito = st.selectbox('Histórico de Créditos',("Sem Débitos","Débitos Pendentes"))
    result =""

    #Quando o Usuário clicar no botão "Verificar" o modelo faz seu trabalho
    if st.button("Verificar"):
        result = prediction(sexo, estado_civil, renda, emprestimo, historico_credito)
        st.success('O empréstimo foi {}'.format(result))
        print(emprestimo)

if __name__=='__main__':
    main()
