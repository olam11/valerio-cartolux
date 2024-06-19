import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='CARTOLUX',
    page_icon=':world_map:',
    menu_items= {"about":"Ceci est un site web en cours de développement"},
    )
st.title("CARTOLUX")
st.write("""****Vous avez plus d'un à essayer de dessiner une carte pendant longtemps...en vain. Mais aussi à en rêver pour décorer un espace, agrémenter vos œuvres littéraires etc. Ne perdez plus votre temps! Dès aujourd'hui, faites confiance à CARTOLUX !****""")
st.write("""
         Nos nombreux styles vous permettront de créer votre carte sur-mesure.
Grâce à nos options, personnalisations et suppléments, ordonnez vôtre carte!    
P.S. : en cas de besoin, contactez-nous!
1) ##### **Fantasy**  
    Le style fantasy est un style cartographique regroupant plus de concepts artistiques que cartographiques.   
    Le fantasy demeure cependant un style de cartographie. 
    Celui-ci est parfaitement adapté aux cartes figurant et agrémentant la lecture dans un ouvrage imaginaire, fantasy ou autre
    Laissez vous séduire par sa complexité et sa sobriété unique. Un style parfaitement modulable selon vos envies.     
    Formats compatibles: A5; A4; A3     
    Prix: entre 0.50 et 2 € + format     \n
    ##### **Images que tu photographieras vendredi.**\n
2) ##### **Atlas**    
    Ce style de cartographie particulier est une compilation d'une carte politique, physique, routière, démographique, etc.
    Contrairement à d'autres styles, une carte atlas sera fort lumineuse, vivement colorée avec des pigments choisis et gorgée d'informations (simplifiables ou pas selon vos choix).
    Son style de conception et son adaptabilité à tous les formats sont ses atouts majeurs.
    Laissez vous guider par ce style sans nul autre égal.       
    Format compatibles: A5; A4; A3; A2      
    Prix entre: 0.75 et 5 € + format\n   
    ##### **3 images**
""")

#image = Image.open("Carte_de_France_de_Mathias_Robert_de_Hesseln_de_1780_(haute_résolution).jpg")
#st.image(image)
