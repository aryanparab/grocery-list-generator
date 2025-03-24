import streamlit as st
import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests
from streamlit_google_auth import Authenticate

st.set_page_config (
    page_title="Hermes List",
    page_icon="🧾",
    layout="wide"
)

authenticator = Authenticate(
    secret_credentials_path='google_secret.json',
    cookie_name='my_cookie_name',
    cookie_key='378228839291001039191030201',
    redirect_uri=["https://aryanparab-grocery-list-generator-streamlit-app-dxclse.streamlit.app/oauth2callback","http://localhost:8501/oauth2callback"],
)


list_gen_page = st.Page("groc.py", title="Make your Shopping List", icon="🍎")
reciepe_page = st.Page("recepie_gen.py", title="Cook Something Delicious", icon="👨🏻‍🍳")
view_list= st.Page("see_list.py",title="Your Current List",icon="🛒")
reciepe_in=st.Page("see_recipes.py",title="See your reciepes",icon="🍳")


def Login():
    authenticator.check_authentification()
    authenticator.login()
def Logout():
    st.write(f"Hello, {st.session_state['user_info'].get('name')}")
    if st.button("Logut?"):
       
        authenticator.logout()


n = Logout if st.session_state['connected'] else Login
nameee = st.session_state['user_info'].get('name') if  st.session_state['connected'] else ""
pg = st.navigation({
        f"Account {nameee}":[n],
        "AI Generators":[list_gen_page,reciepe_page],
        "Your Lists":[view_list]})
  


pg.run()