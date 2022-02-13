from email.headerregistry import UniqueSingleAddressHeader
from enum import auto
from prompt_toolkit import HTML
import streamlit.components.v1 as components
import streamlit as st
fol1,fol2=st.columns(2)
with fol1:
    st.title("IMCapp")

with fol2:
    st.image("WAPP.png",None,350)

col1,col2=st.columns(2)
with col1:
    talla=st.number_input("Talla en cm",1.0,2.6,1.5,0.1)
    peso=st.number_input("Peso",20,500,60,1)
    #Calcular el IMc hasta presionar un boton 
    imc0=peso/talla**2
    #round se usa para redondear y quitar decimales
    imc=round(imc0,1)
calcular=st.button("Calcular índice de masa corporal")
if calcular==True:
    with col2:
        st.image("fit2.png",None,200)
        imctxt = '<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 30px;">Índice de masa corporal</b>'
        st.markdown(imctxt,unsafe_allow_html=True)
    if imc <= 18.5:
        with col2:
            st.warning(imc)
        insbap='<b style= "text-align:center; font-family:Times; color:#3E9185; font-size: 18px;">Sigue las siguientes recomendaciones para aumentar de peso</b>'
        
        st.markdown(bajopeso,unsafe_allow_html=True)
        st.markdown(insbap, unsafe_allow_html=True)
        st.subheader("https://www.medicalnewstoday.com/articles/es/326685")
    elif imc >= 18.6 and imc <=25:
        with col2:
            st.success(imc)
        normpeso='<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 20px;">Estas en tu peso ideal, sigue así</b>'
        with col2:
            st.markdown(normpeso,unsafe_allow_html=True)
    elif imc >= 25 and imc <=30:
        with col2:
            st.warning(imc)
        normpeso='<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 20px;">Estas en sobrepeso, es importante que bajes de peso para evitar contraer enfermedades como diabetes mellitus e hipertensión arterial</b>'
        with col2:
            st.markdown(normpeso,unsafe_allow_html=True)
    elif imc >= 30 and imc <=35:
        with col2:
            st.error(imc)
        ob1peso='<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 20px;">Obesidad grado I, el riesgo de padecer enfermedades metabólicas es alto, se recomienda disminuir de peso inmediatamente</b>'
        with col2:
            st.markdown(normpeso,unsafe_allow_html=True)
    elif imc >= 35 and imc <=40:
        with col2:
            st.error(imc)
        ob1peso='<b style= "text-align:center; font-family:Times; color:#2980B9; font-size: 20px;">Obesidad grado II, el riesgo de padecer enfermedades metabólicas es muy alto, se recomienda disminuir de peso inmediatamente</b>'
        with col2:
            st.markdown(normpeso,unsafe_allow_html=True)

#comentar todo lo seleccionado con cmd+shift+/
# if imc>=18.5 and imc <=24.9:
#     st.balloons()
#     with col2:
#         st.success(imc)
#         st.write("Tienes un peso excelente",Nombre,' te encuentras dentro del rango normal')
# elif imc<=18.5:
#     with col2:
#         st.warning(imc)
#         st.write("Tienes un peso bajo",Nombre,' se recomienda aumentar de peso')
#     st.subheader ("Intenta estas recomendaciones")
#     st.subheader("https://www.medicalnewstoday.com/articles/es/326685")
# elif imc >=25 and imc <=29.9:
#     with col2:
#         st.warning(imc)
#         st.write("Tienes sobrepeso",Nombre,' se recomienda disminuir de peso, estas en el momento correcto para evitar enfermedades y complicaciones')