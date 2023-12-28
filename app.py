import pandas as pd
import plotly.express as px
import streamlit as st

#Leer el archico csv
car_data = pd.read_csv("vehicles_us.csv") 
st.header('Vehiculos')

hist_button = st.checkbox('Construir un histograma') # crear un botón
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
# crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 


disper_button = st.button('Construir un grafico de dispersión') # crear un botón
        
if disper_button:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
# crear un grafico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

        
# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 