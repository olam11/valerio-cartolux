import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(
    page_title='CARTOLUX',
    page_icon=':world_map:',
    layout='wide'
    )

def afficher_image(nom_image):
    image = Image.open(nom_image)
    st.image(image)

st.title("CARTOLUX")
intro = """
###### ***Des cartes comme vous les souhaitez !***\n  
---       
****Vous avez plus d'une fois essayé de dessiner une carte, pendant longtemps...en vain. Mais aussi en rêver pour décorer un espace, agrémenter vos œuvres littéraires...      
Ne perdez plus votre temps! Dès aujourd'hui, faites confiance à CARTOLUX !****\n
---
:red[Admirez] la délicatesse d'un trait précis et net retraçant la carte de votre choix.             
:red[Exaltez-vous] face au réalisme et à la beauté des œuvres que vous commanderez.      
:red[Réjouissez-vous] de la beauté de nos cartes pour leur prix incroyablement bas.       
:red[Soyez surpris] par les multiples possibilités d'une carte paramétrable.        
:red[Ayez confiance] en vos cartographes polyvalents maîtrisant tous les types de carte.        
:red[Jouissez] de nos nombreux styles et formats que vous offrent la carte qui vous convient le mieux.\n
---
### STYLES
Nos nombreux styles vous permettront de créer votre carte sur-mesure.      
Grâce à nos options, personnalisations et suppléments, commandez votre carte !      
:red[Les styles sont gratuits !]      
P.S. : en cas de besoin, contactez-nous!\n\n
"""
fantasy = """ 
Le style fantasy est un style cartographique regroupant plus de concepts artistiques que cartographiques.   
Le fantasy demeure cependant un style de cartographie. 
Celui-ci est parfaitement adapté aux cartes agrémentant la lecture dans un ouvrage imaginaire, fantasy ou autre.     
Laissez vous séduire par sa complexité et sa sobriété unique. Un style parfaitement modulable selon vos envies.     
Formats compatibles: A5; A4; A3      \n
"""

atlas = """  
Ce style de cartographie particulier est une compilation d'une carte politique, physique, routière, démographique...
Contrairement à d'autres styles, une carte atlas sera fort lumineuse, vivement élaborée avec des pigments choisis et gorgée d'informations (simplifiables ou pas selon vos choix).
Son style de conception et son adaptabilité à tous les formats sont ses atouts majeurs.
Laissez vous guider par ce style sans nul autre égal.       
Format compatibles: A5; A4; A3; A2\n     

"""    
     
minimalist = """    
Ce style permet de réduire à l'essentiel le complexe (tout l'inverse d'un Atlas, il sera plus nu, moins vif mais très compréhensible et aéré).
Avec peu de traits et de tons, ce style permet d'identifier les forêts denses, les villes etc. Son charme est sa simplicité et sa façon de faire deviner la matière. Ses attributs permettent d'en faire un carte des plus maniables existantes : sa libre nomenclature, ses polices de texte associées, ses environnements,...      
Formats compatibles: A5; A4; A3; A2\n
"""
options = """---
 ##### **Options**  
:red[Les options sont des suppléments améliorant considérablement la qualité de votre carte. Celles-ci ont un prix qui sera additionné au prix initial de la carte. Si plusieures options sont prises, celles-ci doivent être cumulées.
Les options sont classées en différents types (couleurs et réalisme). On ne peut sélectionner qu'une option par type. Ces options fonctionnent par paliers détaillés dans leur catégorie respective.]
1) ###### **Couleurs**        
    Couleur+    
    L'option couleur+ est l'une des deux options de couleurs.Les options de couleur indiquent un changement de technique et de matériel.L'option couleur+ garantit une majeur réflexion concernant le choix des couleurs et leur rôle dans la carte mais aussi l'utilisation de crayons de couleurs à l'eau pour un meilleur rendu final.   
    Prix : 0,25 €\n
    
    Deluxe couleur      
    Cette option, comme les autres options de couleur, n'est pas compatible avec tous les styles (ex.: Fantasy).
    Le supplément Deluxe couleur est une version réduite du supplément Deluxe intégral. Le Deluxe couleur ne s'étend que sur le côté graphique coloré de la carte. Incluant la formule couleur+, se rajoute une autre technique: les feutres à l'eau (des tonalités plus faibles que les feutres à alcool mais quand même assez visibles. En cas de doute, je suis là pour répondre à toutes vos questions et vous aider à trouver la solution qui vous convient le mieux). Son autre avantage sera l'attention toute particulière portée à l'agencement des couleurs en fonction de leur présence et de leur rôle dans la carte, l'objectif étant d'obtenir un visuel final des plus raffinés où les couleurs créeent ensemble une parfaite harmonie.\n
"""

st.write(intro)
with st.expander("**Fantasy**"):
    st.write(fantasy)
    col1,col2,col3 = st.columns(3)
    with col1:
        afficher_image("IMG_2393.jpg")
    with col2:
        afficher_image("IMG_2387.jpg")
    with col3:
        afficher_image("IMG_2392.jpg")
with st.expander("**Atlas**"):
    st.write(atlas)
    col3,col1,col2,col4 = st.columns([1,2.5,2,1],gap="large",vertical_alignment="center")
    with col1:
        afficher_image("IMG_2394.jpg")
    with col2:
        afficher_image("IMG_2395.jpg")
with st.expander("**Minimalist**"):    
    st.write(minimalist)
    col3,col1,col2,col4 = st.columns([1,2.5,2,1],gap="large",vertical_alignment="center")
    with col1:
        afficher_image("IMG_2388.jpg")
    with col2 :
        afficher_image("IMG_2391.jpg")

st.write(options)

# st.write("---\n### TARIFS\n")

# df = {
#         "format" : ["A5", "A4", "A3","A2"],
#         "simple" : ["0,75 €", "1 €", "3 €","5,50 €"],
#         "deluxe couleurs" : ["0,50 €","0,50 €","1,50 €","3 €"],
#         "deluxe intégral" : ["0,50 €","1€","2 €","3,50 €"],
#         "réalisme +" :["0,25 €","0,50 €","1 €","2,50 €"],
#         "couleur +" :["0,50 €","0,50 €","0,50 €","0,50 €"],
#         "éléments princ.":["0,50 €","0,50 €","0,50 €","0,50 €"],
#         "éléments sec.":["0,25 €","0,25 €","0,25 €","0,25 €"],
#      }

# df = pd.DataFrame.from_dict(df, orient='index')
# df = df.transpose()
# st.dataframe(df, use_container_width=True,hide_index=True)
grille_de_prix = {"A5":[0.75,0.50,0.50,0.25,0.50,0.50,0.25],"A4":[1,0.50,1,0.50,0.50,0.50,0.25],"A3":[3,1.50,2,1,0.50,0.50,0.25],"A2":[5.50,3,3.50,2.50,0.50,0.50,0.25]}
# st.write("##### **+ 0,25 € par heure de travail**\n---")

st.write("---")
st.write("### SIMULATION")
with st.form("simulation"):
    format = st.selectbox(
    "###### le format :",
    ("A5", "A4", "A3","A2"))
    checkbox_couleurs = st.checkbox("deluxe couleurs" )
    checkbox_integral = st.checkbox("deluxe intégral" )
    checkbox_realismeplus = st.checkbox("réalisme +" )
    checkbox_couleurplus = st.checkbox("couleur +" )
    element_princ = st.slider("éléments princ.",0,10,0)
    element_sec = st.slider("éléments sec.",0,10,0)
    submitted = st.form_submit_button("Voir l'estimation")
    if submitted:
        listdeprixparformat = grille_de_prix[format]
        prix = listdeprixparformat[0]
        commande = [f"format : {format}"]
        if checkbox_couleurs == True:
            prix = prix+listdeprixparformat[1]
            commande.append("Deluxe couleurs")
        if checkbox_integral == True:
            prix = prix+listdeprixparformat[2]
            commande.append("Deluxe intégral")
        if checkbox_realismeplus == True:
            prix = prix+listdeprixparformat[3]
            commande.append("réalisme +")
        if checkbox_couleurplus == True:
            prix = prix+listdeprixparformat[4]
            commande.append("couleur +")
        prix = prix+element_princ*listdeprixparformat[5]
        prix = prix+element_sec*listdeprixparformat[6]
        prix = str(prix)+" €"
        resume_estimation = prix
        st.write(f"###### Estimation du prix : {prix}")
        st.write("**+ 0,25 € par heure de travail**")
        st.write("Pour :")
        for i in range(len(commande)):
            st.write("-"+commande[i])
            resume_estimation = resume_estimation+" "+commande[i]
        if element_princ != 0:
            st.write(f"-{element_princ} élément(s) principal(aux)")
            resume_estimation = resume_estimation+" "+f"{element_princ} élément(s) principal(aux)"
        if element_sec != 0:
            st.write(f"    -{element_sec} élément(s) secondaire(s)")
            resume_estimation = resume_estimation+" "+f"{element_sec} élément(s) secondaire(s)"   
            
st.write("---")
st.subheader("Liens")
st.page_link(page="https://motdepassedelinfini.streamlit.app/",label="Le mot de passe de l'infini",icon="♾️")
st.page_link(page="https://github.com/olam11",label="Mon Github",icon="🐙")
st.page_link(page="https://github.com/olam11/valerio-cartolux",label="Le repo de ce site",icon="🗺️")