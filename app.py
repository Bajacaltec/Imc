import streamlit as st
col1,col2=st.beta_columns(2)
with col1:
    st.image("mp.jpeg",None,300)
with col2:
    st.image('WAPP.png',None,)
col1,col2=st.beta_columns(2)
with col1:
    Nombre=st.text_input("¿Como te llamas?")
    genero=st.selectbox("Género",["Femenino","Masculino"])
    edad=st.slider("Edad",16,120,18,1)
    bienvenida="Bienvenida "+Nombre+ " iniciaremos con algunas preguntas"
    bienvenido="Bienvenido "+Nombre+ " iniciaremos con algunas preguntas"
inicio=st.button("Empecemos")

if inicio==True and genero=="Femenino":
    st.success(bienvenida)
elif inicio==True and genero=="Masculino":
    st.success(bienvenido)
with col2:
    st.image("fit2.png",None,300)
