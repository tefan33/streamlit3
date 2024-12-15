# penser à utilser le prompt de anaconda : streamlit run stephan_streamlit_3.py

import streamlit as st
from streamlit_authenticator import Authenticate

# Importation du module
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': 
                        {
                        'utilisateur': 
                            {'name': 'utilisateur',
                            'password': 'utilisateurMDP',
                            'email': 'utilisateur@gmail.com',
                            'failed_login_attemps': 0, # Sera géré automatiquement
                            'logged_in': False, # Sera géré automatiquement
                            'role': 'utilisateur'
                            },
                        'root': 
                            {'name': 'root',
                            'password': 'rootMDP',
                            'email': 'admin@gmail.com',
                            'failed_login_attemps': 0, # Sera géré automatiquement
                            'logged_in': False, # Sera géré automatiquement
                            'role': 'administrateur'
                            }
                        }
                    }

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():    
# Using "with" notation

    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos"]
        )

    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        st.title("Bienvenu sur le contenu réservé aux utilisateurs connectés")
    elif selection == "Photos":
        st.title("Bienvenue sur mon album photo de Noël")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Cuisine")
            st.image("https://images.pexels.com/photos/16471876/pexels-photo-16471876/free-photo-of-pain-nourriture-aliments-table.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

        with col2:
            st.header("Salon")
            st.image("https://images.pexels.com/photos/5847901/pexels-photo-5847901.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")

        with col3:
            st.header("Chambre")
            st.image("https://images.pexels.com/photos/29749442/pexels-photo-29749442/free-photo-of-scene-de-fete-avec-bougies-et-decoration.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")


if st.session_state["authentication_status"]:
    accueil()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')