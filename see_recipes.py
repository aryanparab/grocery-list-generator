import streamlit as st
from  datetime import datetime
import json
import random
import time

def convert(date_time):
    format = '%a %b %d %H:%M:%S %Y'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str


    

with open('my_reciepes.json', 'r') as file:
    recipe_data = json.load(file)

st.title("Hermes' List🧾")
st.subheader("Your Current Recipes")

get_recent = list(recipe_data.keys())[0]
get_recent_time = convert(get_recent)

for i in list(recipe_data.keys()):
    if get_recent_time<convert(i):
        get_recent = i

with st.form("prev_lists"):
    your_lists = st.selectbox("Veiw Previous Recipes? ",options=list(recipe_data.keys()))
    submit = st.form_submit_button("View")


if submit:
    get_recent = your_lists

st.write(get_recent)
st.write(recipe_data[get_recent])
