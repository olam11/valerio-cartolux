import streamlit as st

# configuration de la page
st.set_page_config(
    page_title='CARTOLUX',
    page_icon=':world_map:',
    layout='wide'
    )

    
with st.sidebar:
    st.page_link(page="https://motdepassedelinfini.streamlit.app/",label="Le mot de passe de l'infini",icon="♾️")
    st.page_link(page="https://github.com/olam11",label="Mon Github",icon="🐙")
    st.page_link(page="https://github.com/olam11/valerio-cartolux",label="Le repo de ce site",icon="🗺️")
    
pages = [st.Page("onglets/accueil.py", title="Accueil",icon=":material/home:"),
        st.Page("onglets/styles.py", title="Styles",icon=":material/border_color:"),
        st.Page("onglets/commande.py", title="Commande", icon=":material/package:")]

pg = st.navigation(pages)
pg.run()
