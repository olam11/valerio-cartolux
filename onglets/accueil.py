import streamlit as st
from PIL import Image
from streamlit_carousel import carousel

st.title("CARTOLUXE")
intro = """
###### ***Des cartes comme vous les souhaitez !***\n  
---
"""
suite_intro = """
****Vous avez plus d'une fois essayé de dessiner une carte, pendant longtemps...en vain. Mais aussi en rêver pour décorer un espace, agrémenter vos œuvres littéraires...      
Ne perdez plus votre temps ! Dès aujourd'hui, faites confiance à CARTOLUXE !****\n\n
:red[Admirez] la délicatesse d'un trait précis et net retraçant la carte de votre choix.             
:red[Exaltez-vous] face au réalisme et à la beauté des œuvres que vous commanderez.      
:red[Réjouissez-vous] de la beauté de nos cartes pour leur prix incroyablement bas.       
:red[Soyez surpris] par les multiples possibilités d'une carte paramétrable.        
:red[Ayez confiance] en vos cartographes polyvalents maîtrisant tous les types de carte.        
:red[Jouissez] de nos nombreux styles et formats que vous offrent la carte qui vous convient le mieux.\n
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
col1,col2 = st.columns(2,vertical_alignment="top")
with col1:
    st.write(suite_intro)
    # st.page_link(page="onglets/styles.py",label="Découvrir nos magnifiques styles",icon=":material/border_color:")
    if st.button(":material/border_color: Découvrir nos magnifiques styles",use_container_width=False):
        st.switch_page("onglets/styles.py")
with col2:
    items = [
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2392.jpg",
    ),
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
        img="images/IMG_2388.jpg",
    ),
    dict(
        title=" ",
        text=" ",
        img="images/IMG_2391.jpg",
    ),
    dict(
        title="",
        text=" ",
        img="images/IMG_2394.jpg",
    ),
    dict(
        title="",
        text=" ",
        img="images/IMG_2395.jpg",
    ),
    dict(
        title="",
        text=" ",
        img="images/IMG_2396.jpg",
    ),
]

                
    carousel(items=items)


            

