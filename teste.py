import streamlit as st

st.title('Teste ECMI 2')
st.write("Esse é o meu texto")

nome = st.text_input('Digite o seu nome')
if nome:
  st.write(nome, 'é uma menina legal!')



st.image('https://conhecimentocientifico.r7.com/wp-content/uploads/2020/09/praias-o-que-sao-caracteristicas-e-importancia-para-o-meio-ambiente-5.jpg.webp')

