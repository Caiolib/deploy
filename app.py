import streamlit as st
import requests
from PIL import Image


url = "https://restcountries.com/v3.1"


st.title("Informações do País")

#Nome oficial do país.
#Países com os quais faz fronteira.
#Latitude e longitude do país.


pais = st.text_input("País:")
if st.button("Buscar Pais"):
    response = requests.get(f"{url}/name/{pais}?fullText=true").json()
    with st.expander("See explanation"):
        
        col1, col2= st.columns(2)
        print(response)
        objeto = response[0]
        nome_oficial = (objeto['name']['official'])
        Latitudo = objeto['latlng'][0]
        longitude = objeto['latlng'][1] 
        fronteiras = objeto['borders']
        bandeira = objeto['flags']['png']
        brasao = objeto['coatOfArms']['png']
        with col1:
            st.header(f'Nome oficial: {nome_oficial}')
            st.text(f'Paises que faz fronteira:{fronteiras}')
            st.text(f"Latitude : {Latitudo}, longitude : {longitude}")

        with col2:
            if brasao:
                st.image(brasao, width=400)
        st.image(bandeira, use_column_width=col2)
    
        