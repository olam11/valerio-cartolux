import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
st.set_page_config(
    page_title='CARTOLUX',
    page_icon=':world_map:',
    layout='wide',
    menu_items= {"about":"Ceci est un site web en cours de développement"},
    )
st.title("CARTOLUX")
st.write("""
###### ***:rainbow[Des carte comme vous les souhaitez !]***\n         
****Vous avez plus d'un à essayer de dessiner une carte pendant longtemps...en vain. Mais aussi à en rêver pour décorer un espace, agrémenter vos œuvres littéraires etc.       
Ne perdez plus votre temps! Dès aujourd'hui, faites confiance à CARTOLUX !****\n
:red[Admirez] la délicatesse d'un trait précis et net retraçant la carte de votre choix.             
:red[Exaltez-vous] face au réalisme et à la beauté des œuvres que vous commanderez.      
:red[Réjouissez-vous] du magnifique de nos cartes pour leur prix minimes.       
:red[Soyez surpris] par la multiple possibilité de votre carte paramédiable.        
:red[Soyez confiant] en vos cartographes polyvalents maîtrisant tous les types de carte.        
:red[Jouissez] de nos nombreux styles et formats que vous offrentla carte qui vous convient le mieux.\n
### STYLES
Nos nombreux styles vous permettront de créer votre carte sur-mesure.      
Grâce à nos options, personnalisations et suppléments, ordonnez vôtre carte!   
P.S. : en cas de besoin, contactez-nous!\n\n

1) ##### **Fantasy**  
    Le style fantasy est un style cartographique regroupant plus de concepts artistiques que cartographiques.   
    Le fantasy demeure cependant un style de cartographie. 
    Celui-ci est parfaitement adapté aux cartes figurant et agrémentant la lecture dans un ouvrage imaginaire, fantasy ou autre
    Laissez vous séduire par sa complexité et sa sobriété unique. Un style parfaitement modulable selon vos envies.     
    Formats compatibles: A5; A4; A3     
    Prix: entre 0.50 et 2 € + format     \n
2) ##### **Atlas**    
    Ce style de cartographie particulier est une compilation d'une carte politique, physique, routière, démographique, etc.
    Contrairement à d'autres styles, une carte atlas sera fort lumineuse, vivement colorée avec des pigments choisis et gorgée d'informations (simplifiables ou pas selon vos choix).
    Son style de conception et son adaptabilité à tous les formats sont ses atouts majeurs.
    Laissez vous guider par ce style sans nul autre égal.       
    Format compatibles: A5; A4; A3; A2      
    Prix entre: 0.75 et 5 € + format\n   
    
### TARIFS\n
""")
df = {
        "format" : ["A5", "A4", "A3","A2"],
        "simple" : ["0,75 €", "1 €", "3 €","5,50 €"],
        "deluxe couleurs" : ["0,50 €","0,50 €","1,50 €","3 €"],
        "deluxe intégral" : ["0,50 €","1€","2 €","3,50 €"],
        "réalisme +" :["0,25 €","0,50 €","1 €","2,50 €"],
        "couleur +" :["0,50 €","0,50 €","0,50 €","0,50 €"],
        "éléments princ.":["0,50 €","0,50 €","0,50 €","0,50 €"],
        "éléments sec.":["0,25 €","0,25 €","0,25 €","0,25 €"],
     }

df = pd.DataFrame.from_dict(df, orient='index')
df = df.transpose()
st.dataframe(df, use_container_width=True,hide_index=True)
st.markdown(df.to_html(escape=False),unsafe_allow_html=True)
st.info("on garde lequel ?")

#image = Image.open("Carte_de_France_de_Mathias_Robert_de_Hesseln_de_1780_(haute_résolution).jpg")
#st.image(image)
