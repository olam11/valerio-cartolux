import streamlit as st
from Carte_de_France_de_Mathias_Robert_de_Hesseln_de_1780_(haute_résolution) import*

st.set_page_config(
    page_title='CARTOLUX',
    page_icon=':world_map:',
)
st.title("CARTOLUX")
st.write("Ceci est un site web en cours de développement pour Valerio Delsart Moretti")
image = Carte_de_France_de_Mathias_Robert_de_Hesseln_de_1780_(haute_résolution).jpg
st.image(image)
