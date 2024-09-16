import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

def afficher_image(nom_image):
    image = Image.open(nom_image)
    st.image(image)

styles_présentation = """
Nos nombreux styles vous permettront de créer votre carte sur-mesure.      
Grâce à nos options, personnalisations et suppléments, commandez votre carte !      
**Les styles sont gratuits !**\n\n
"""
fantasy = """ 
Le style fantasy est un style cartographique regroupant plus de concepts artistiques que cartographiques.   
Le fantasy demeure cependant un style de cartographie. 
Celui-ci est parfaitement adapté aux cartes agrémentant la lecture dans un ouvrage imaginaire, fantasy ou autre.     
Laissez vous séduire par sa complexité et sa sobriété unique. Un style parfaitement modulable selon vos envies.     \n
"""

atlas = """  
Ce style de cartographie particulier est une compilation d'une carte politique, physique, routière, démographique...
Contrairement à d'autres styles, une carte atlas sera fort lumineuse, vivement élaborée avec des pigments choisis et gorgée d'informations (simplifiables ou pas selon vos choix).
Son style de conception et son adaptabilité à tous les formats sont ses atouts majeurs.
Laissez vous guider par ce style sans nul autre égal.       \n     

"""    
     
minimalist = """    
Ce style permet de réduire à l'essentiel le complexe (tout l'inverse d'un Atlas, il sera plus nu, moins vif mais très compréhensible et aéré).
Avec peu de traits et de tons, ce style permet d'identifier les forêts denses, les villes etc. Son charme est sa simplicité et sa façon de faire deviner la matière. Ses attributs permettent d'en faire un carte des plus maniables existantes : sa libre nomenclature, ses polices de texte associées, ses environnements,...      \n
"""
st.title("STYLES")
st.write(styles_présentation)
st.divider()

col1,col2 = st.columns([1,2],vertical_alignment='center')
with col1: 
    st.subheader("Atlas")
    st.write(atlas)
    # st.page_link("onglets/commande.py", label="Commander", icon=":material/package:")
    if st.button(":material/package: Commander",use_container_width=True,key="button_commander_1"):
        st.switch_page("onglets/commande.py")
        
with col2:
    items = [
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2394.jpg",
    ),
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2395.jpg",
    ),
]

            
    carousel(items=items)
st.divider()
col1,col2 = st.columns([1,2],vertical_alignment="center")
with col1: 
    st.subheader("Minimalist")
    st.write(minimalist)
    # st.page_link("onglets/commande.py", label="Commander", icon=":material/package:")
    if st.button(":material/package: Commander",use_container_width=True,key="button_commander_2"):
        st.switch_page("onglets/commande.py")
with col2:
    items = [
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2388.jpg",
    ),
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2391.jpg",
    ),
]

            
    carousel(items=items)
st.divider()
col1,col2 = st.columns(2,vertical_alignment='center')
with col1: 
    st.subheader("Fantasy")
    st.write(fantasy)
    # st.page_link("onglets/commande.py", label="Commander", icon=":material/package:")
    if st.button(":material/package: Commander",use_container_width=True,key="button_commander_3"):
        st.switch_page("onglets/commande.py")
with col2:
    items = [
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2393.jpg",
    ),
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2387.jpg",
    ),
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2392.jpg",
    ),]
    
    carousel(items=items)


