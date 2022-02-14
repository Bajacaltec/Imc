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
    riesgo=st.selectbox("Tienes alguna enfermedad",["No","Si"])
    #Calcular el IMc hasta presionar un boton 
    imc0=peso/talla**2
    #round se usa para redondear y quitar decimales
    imc=round(imc0,1)

with col2:
        st.image("fit2.png",None,200,auto)
calcular=st.button("Calcular índice de masa corporal",)
wol1,wol2=st.columns(2)
if calcular==True:
    if imc < 18.5:
        with wol1:
            st.subheader('IMC (m2)')
            st.warning(imc)
        with wol2:
            st.info("Tu índice de masa corporal indica un bajo peso para tu talla, es necesario aumentar tu peso, sigue las recomendaciones de la liga mostrada abajo")
        st.subheader("https://www.medicalnewstoday.com/articles/es/326685")
    elif imc >= 18.5 and imc <=25:
        with wol1:
            st.subheader('IMC (m2)')
            st.success(imc)
        with wol2:
            st.info("Estas en tu peso ideal, continua con buena alimentación y ejercicio diario, recuerda que el consumo de alcohol y tabaco puede generar enfermedades incluso si mantienes tu peso ideal") 
        st.balloons()
    elif imc >= 25 and imc <=30:
        with wol1:
            st.subheader('IMC (m2)')
            st.warning(imc)
        with wol2:
            st.info("Te encuentras en sobrepeso, el riesgo de contraer enfermedades metabólicas, aumenta progresivamente con el tiempo y el aumento de peso, es importante que inicies una reducción de peso para evitar problemas de salud en el futuro") 
    elif imc >= 30 and imc <=35:
         with wol1:
            st.subheader('IMC (m2)')
            st.warning(imc)
         with wol2:
            st.info("Te encuentras en obesidad grado I, el riesgo de contraer enfermedades metabólicas es inminente, tu riesgo cardiovascular se elevará de continuar así poniendote en riesgo de un infarto agudo al miocardio, además el deterioro en la calidad de vida se ve con el aumento de peso") 
         if riesgo=='Si':
             st.info("Puedes ser candidatos a cirugía bariátrica, para reducir peso, evitar complicaciones de tus enfermedades de base e incluso curarlas")
             with wol1:
                 st.info("https://www.topdoctors.mx/cirugia-bariatrica-especialidad/")

    elif imc >= 35 and imc <=40:
        with wol1:
            st.subheader('IMC (m2)')
            st.warning(imc)
            st.info("https://www.topdoctors.mx/cirugia-bariatrica-especialidad/")

        with wol2:
            st.error("Obesidad grado II, el riesgo de padecer enfermedades metabólicas es muy alto, se recomienda disminuir de peso inmediatamente")
            st.info("La cirugía bariátrica para reducción de peso esta indicada, contacta a un cirujano bariatra certificado para valoración")

    elif imc >= 40:
        with wol1:
            st.subheader('IMC (m2)')
            st.warning(imc)
            st.info("https://www.topdoctors.mx/cirugia-bariatrica-especialidad/")

            
        with wol2:
            st.error("Obesidad grado III, el riesgo de padecer enfermedades metabólicas es muy alto, se recomienda disminuir de peso inmediatamente")
            st.info("La cirugía bariátrica para reducción de peso esta indicada, contacta a un cirujano bariatra certificado para valoración")
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