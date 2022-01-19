from prompt_toolkit import HTML
import streamlit.components.v1 as components
import streamlit as st
st.image('WAPP.png',None)
col1,col2=st.columns(2)
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
#if imc >24.9 and imc <29.9:
 #   st.write(Nombre," tienes un IMC dentro de los niveles superiores, estas a buen momento de reducir tu peso con ejercicio y dieta para evitar complicaciones futuras y evitar enfermedades como diabetes e hipertensión")
