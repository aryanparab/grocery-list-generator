import streamlit as st
from  datetime import datetime
import json
import random
import time

def convert(date_time):
    format = '%a %b %d %H:%M:%S %Y'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str

def view_list(get_recent):
    shopping_dict = shopping_data[get_recent][0]
    list_data = shopping_data[get_recent][1]
    store_costs =  [sum(price for item, price in shopping_dict[i]) for i in shopping_dict] 
    total_cost = sum(store_costs)
    st.caption(get_recent)
    st.subheader(f"Total Cost: ${total_cost:.2f}")
    for n,i in enumerate(shopping_dict):
            r = random.randint(0,10000000000)
            st.subheader(f"{i} - ${store_costs[n]:.2f}")
            for item,price in shopping_dict[i]:
                st.checkbox(f"{item} - ${price}",key=f"{item}-{price}-{time.ctime()}-{r}")

    

with open('shopping_list.json', 'r') as file:
    shopping_data = json.load(file)

st.title("Hermes' List🧾")
st.subheader("Your Current shopping list")

get_recent= [i for i,j in shopping_data.items() if j[2]=="curr"][0]
get_recent_time = convert(get_recent)

with st.form("prev_lists"):
    your_lists = st.selectbox("Veiw other lists? ",options=list(shopping_data.keys()))
    submit = st.form_submit_button("View")


if submit:
    get_recent = your_lists


view_list(get_recent)
