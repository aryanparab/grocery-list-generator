from ing import cuisine_ingredients
from chef import cooker
import streamlit as st
import time
from datetime import datetime
import ast
import json

st.title("Hermes' List🧾")
st.subheader("Create a Meal Plan🍳🗓️")
st.caption("Let's create a meal plan based on your grocery list👨🏻‍💻")

with open("my_reciepes.json",'r') as file:
    reciepes = json.load(file)

def convert(date_time):
    format = '%a %b %d %H:%M:%S %Y'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str

with open('shopping_list.json', 'r') as file:
    shopping_data = json.load(file)



get_recent= list(shopping_data.keys())[0]
get_recent_time = convert(get_recent)

for i in shopping_data.keys():
    if get_recent_time < convert(i):
         get_recent = i

shopping_dict = shopping_data[get_recent]
items = shopping_dict[0]
inputs = shopping_dict[1]

try:
    reciepe = reciepes[get_recent]

except:
        get_recent_rec=""
        reciepe = ""

statement =f"""
The recipes displayed are for a duration of {inputs[0]} weeks. They include the following - {",".join(inputs[1])}.
You will be provided recipes for : {",".join(inputs[2])}. No: of servings per meal : {inputs[3]}.
Your selected cuisine preferences are : {",".join(inputs[5])}
"""

prompt = st.text_area(value=statement,label="",height=150)
gen = st.button("Generate new?")
if gen:
    new_rec = cooker(prompt+"  Grocery list : " + str(items))
    st.write(new_rec)
   
    if get_recent_rec =="":
        reciepes.update({get_recent: new_rec})
    else:
        reciepes[get_recent]= new_rec
    with open("my_reciepes.json","w") as file:
        json.dump(reciepes,file,indent=4)
else:
    st.write(reciepe)