from prompt_toolkit import HTML
import streamlit.components.v1 as components
import streamlit as st
st.image('WAPP.png',None)
col1,col2=st.beta_columns(2)
with col1:
    Nombre=st.text_input("¿Como te llamas?")
    genero=st.selectbox("Género",["Femenino","Masculino"])
    comorb=st.multiselect("Tienes alguna enfermedad",['Ninguna',"Diabetes mellitus","Hipertensión arterial (presión alta)","Problemas cardiacos","Hígado graso","Dislipidemia (Problemas de lípidos)"],"Ninguna")
    edad=st.slider("Edad",10,120,18,1)
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

if imc>=18.5 and imc <=24.9:
    st.balloons()
    with col2:
        st.success(imc)
        st.write("Tienes un peso excelente",Nombre,' te encuentras dentro del rango normal')
elif imc<=18.5:
    with col2:
        st.warning(imc)
        st.write("Tienes un peso bajo",Nombre,' se recomienda aumentar de peso')
    st.subheader ("Intenta estas recomendaciones")
    st.subheader("https://www.medicalnewstoday.com/articles/es/326685")
elif imc >=25 and imc <=29.9:
    with col2:
        st.warning(imc)
        st.write("Tienes sobrepeso",Nombre,' se recomienda disminuir de peso, estas en el momento correcto para evitar enfermedades y complicaciones')
elif imc >=30 and imc <=34.9 and "Ninguna" in comorb:   
    with col2:
        st.warning(imc)
        st.write("Tienes obesidad grado I",Nombre,' se recomienda disminuir de peso, estas en un alto riesgo para enfermedades metabólicas y enfermedades cardiovasculares')
