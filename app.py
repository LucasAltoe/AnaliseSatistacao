import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#NLTK - Natural Language Language Tool Kit
import nltk

#O sistema terá 3 fases: 1 - Criação do sistema, 2 - Criação da MP/PLN, 3 - Utilização do sistema

#Fase 1:

#título do sistema
st.write(" # Análise de Satisfação do Cliente")

#entrada de dados / manifestação do cliente
user_input = st.text_input("Por favor, avalie o nosso trabalho   :  ")

#Fase 2: 

nltk.download('vader_lexicon')
Satisfacao = SentimentIntensityAnalyzer() # Máquina preditiva é criada
score = Satisfacao.polarity_scores(user_input)

if score == 0:
    st.write("Análise Neutra")
elif score ["neg"] != 0:
    st.write("Análise Negativa")
elif score ["pos"] != 0:
    st.write("Análise Positiva")

#Fase 3: 

#streamlit run app.py
