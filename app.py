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
    talla=st.number_input("Talla en cm",1.0,2.6,1.5,0.1)
    peso=st.number_input("Peso",20,500,60,1)
    imc0=peso/talla**2
    #round se usa para redondear y quitar decimales
    imc=round(imc0,1)


with col2:
    st.image("fit2.png",None,300)
    imctxt = '<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 30px;">Índice de masa corporal</b>'
    st.markdown(imctxt,unsafe_allow_html=True)
    st.success(imc)

