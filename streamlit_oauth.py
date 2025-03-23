import streamlit as st
import authlib
from streamlit_google_auth import Authenticate

# st.title("Streamlit OAuth Playground")
# if not st.experimental_user.is_logged_in:
#     if st.button("Log in with Google", type="primary", icon=":material/login:"):
#         st.login()
# else:
#     st.logout()

# st.caption(f"Streamlit version {st.__version__}")
# st.caption(f"Authlib version {authlib.__version__}")

authenticator = Authenticate(
    secret_credentials_path='google_secret.json',
    cookie_name='my_cookie_name',
    cookie_key='378228839291001039191030201',
    redirect_uri='http://localhost:8501',
)

authenticator.check_authentification()

# Display the login button if the user is not authenticated
authenticator.login()

# Display the user information and logout button if the user is authenticated
if st.session_state['connected']:
    st.image(st.session_state['user_info'].get('picture'))
    st.write(f"Hello, {st.session_state['user_info'].get('name')}")
    st.write(f"Your email is {st.session_state['user_info'].get('email')}")
    if st.button('Log out'):
        authenticator.logout()