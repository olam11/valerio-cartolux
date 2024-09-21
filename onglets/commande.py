import streamlit as st
import re
import smtplib
from email.mime.text import MIMEText
def send_email(body,email_receiver,subject):
    email_sender = st.secrets["email"]["adress"]

    msg = MIMEText(body)
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(st.secrets["email"]["adress"],st.secrets["email"]["password"])
    server.sendmail(email_sender, email_receiver, msg.as_string())
    server.quit()


def deluxe_integral_func():
    st.session_state.disabled = True
    
def convertir_en_euro(montant):
    # Vérifier si le montant est un entier
    if montant.is_integer():
        montant_formate = f"{int(montant)}"
    else:
        montant_formate = f"{montant:.2f}".replace('.', ',')
    return f"{montant_formate} €"

if "disabled" not in st.session_state:
    st.session_state.disabled = False
    
if "deluxe_integral" not in st.session_state:
    st.session_state["deluxe_integral"] = False
    
if st.session_state["deluxe_integral"] == False:
    st.session_state.disabled = False

grille_de_prix = {"A5":[0.75,0.50,0.50,0.25,0.50,0.50,0.25,0.25],"A4":[1,0.50,1,0.50,0.50,0.50,0.25,0.50],"A3":[3,1.50,2,1,0.50,0.50,0.25,1],"A2":[5.50,3,3.50,2.50,0.50,0.50,0.25,2]}
global prix_total
prix_total = 0
st.title("COMMANDE")
st.divider()
st.subheader("Estimation")

style = st.radio(label="Styles",options=["Atlas","Minimalist","Fantasy"])

if style == "Atlas" or style == "Minimalist":
    format = st.radio(label="Format",options=["A5","A4","A3","A2"])
else:
    format = st.radio(label="Format",options=["A4","A3","A2"])
prix_total = prix_total+grille_de_prix[format][0]

couleurs_options = st.radio("Options de couleurs",options=["Simple","Couleurs+","Deluxe couleurs"],help="?",disabled=st.session_state.disabled)
if couleurs_options == "Couleurs+" and st.session_state.disabled == False:
    prix_total = prix_total+0.5
    
elif couleurs_options == "Deluxe couleurs" and st.session_state.disabled == False:
    prix_total = prix_total+grille_de_prix[format][1]
    
options_réalisme = st.radio("Options de réalisme",options=["Simple","Réalisme+"],help="?",disabled=st.session_state.disabled)
if options_réalisme == "Réalisme+" and st.session_state.disabled == False:
    prix_total = prix_total+grille_de_prix[format][3]


deluxe_integral = st.toggle(label="Deluxe integral",help="?",on_change=deluxe_integral_func(),key="deluxe_integral",value=st.session_state.disabled)
if deluxe_integral:
    deluxe_integral_francais = "activé"
    prix_total = prix_total+grille_de_prix[format][2]
else:
    deluxe_integral_francais = "désactivé"
    
col1,col2,col3 = st.columns([1,1,2],vertical_alignment="bottom")

with col1 :
    nb_elements_princ = st.number_input("Eléments principaux (Montagnes,forêts)",min_value=1,max_value=10,step=1,help="Eléments naturels")
    prix_total =prix_total+0.5*nb_elements_princ
with col2 :
    nb_elements_sec = st.number_input("Eléments secondaires (ville,lac,fleuves...)",min_value=1,max_value=10,step=1,help="villes,lacs,fleuves...")
    prix_total =prix_total+0.25*nb_elements_sec
    
prix_total = prix_total+grille_de_prix[format][7]
# prix_total_str = "{:.2f} €".format(prix_total)
prix_total_str = convertir_en_euro(prix_total)
st.write(f"**Estimation du prix : {prix_total_str}**")
st.divider()
st.subheader("Commander")

prenom_user = st.text_input("Votre prénom:red[*]")
nom_user = st.text_input("Votre nom:red[*]")
prenom_user = prenom_user.capitalize()
nom_user = nom_user.capitalize()
st.caption(":red[*]Pour un echange plus cordial avec votre cartographe")
email_user = st.text_input("Votre email")
commentaire = st.text_area("Personnalisation",max_chars=1000,placeholder="La description de votre carte...")
if st.button("Commander pour "+prix_total_str) and email_user and prenom_user and nom_user: 
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_user):
        with st.spinner("En cours d'envoie..."):
            try:
                send_email(
                    body=f"""
Une commande de {prenom_user} {nom_user}:   
style : {style}
format : {format}
options de couleurs : {couleurs_options}
option de réalisme : {options_réalisme}
deluxe intégral : {deluxe_integral_francais}
nombre d'éléments principaux : {str(nb_elements_princ)}
nombre d'éléments secondaires : {str(nb_elements_sec)}
commentaire de personnalisation :   
{commentaire}    
prix total : {prix_total_str}

Email de {prenom_user} {nom_user} : {email_user} 
                    """,
                    email_receiver = st.secrets["email"]["adress"],
                    subject=f"Commande de {prenom_user} {nom_user}"
                    )
                send_email(
                    body=f"""
Votre commande : 
{commentaire}  
En style {style}, en {format} avec les options:
Couleurs : {couleurs_options}
Réalisme : {options_réalisme}
Deluxe intégral : {deluxe_integral_francais}
Vons avez demandé {str(nb_elements_princ)} éléments principaux et {str(nb_elements_sec)} éléments secondaires, pour un total de {prix_total_str}

Cartoluxe

Contact : cartoluxe@gmail.com
                    """,
                    email_receiver = email_user,
                    subject=f"Cartoluxe : confirmation votre commande"
                    )
                st.success("Commande envoyée 👍")
            except Exception as e:
                st.error(f"Erreur dans l'envoie de la commande :\n{e}")   
    else:
        st.caption(":red[Veuillez entrer une email valide !]")
        

