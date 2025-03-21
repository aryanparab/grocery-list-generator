import streamlit as st

list_gen_page = st.Page("groc.py", title="Make your Shopping List", icon="🍎")
reciepe_page = st.Page("recepie_gen.py", title="Cook Something Delicious", icon="👨🏻‍🍳")
view_list= st.Page("see_list.py",title="Your Current List",icon="🛒")
reciepe_in=st.Page("see_recipes.py",title="See your reciepes",icon="🍳")

pg = st.navigation({
    "AI Generators":[list_gen_page,reciepe_page],
    "Your Lists":[view_list,reciepe_in]})
st.set_page_config(page_title="Hermes' List", page_icon="🧾")
pg.run()