
from ing import cuisine_ingredients
from shopper import getter
import streamlit as st
import time
from datetime import datetime
import ast
import json

st.title("Hermes' List🧾")
st.subheader("Let's get your fridge filled!👨‍🌾👨🏻‍🍳")
st.caption("I will help you generate the most optimizied grocery list for your next trip to the market!🛒")

cuisines = list(cuisine_ingredients.keys())
with open('shopping_list.json', 'r') as file:
    shopping_list_memory = json.load(file)

with st.form("my_form"):
    duration=st.number_input("Enter Duration in weeks",min_value=1)
    diet = st.multiselect("Enter dietary preferences/ protien",["Vegetables", "Chicken", "Fish", "Eggs", "Dairy products", "Plant-based"])
    meals =st.multiselect("Select Meals you have",["Lunch","Breakfast","Dinner"])
    servings = st.number_input("Enter no. of servings per meal",min_value=1)
    already_have = st.text_input("Any ingredients that you already have with quantity ? ")
    cusine = st.multiselect("Cuisine Preferences",cuisines,max_selections=4)
    comments = st.text_area("Additional comments that you want to add : ")
    budget = st.text_input(f"Enter your total budget in $")
    submit = st.form_submit_button('Shop On!')


if submit:
    list_data = [duration,diet,meals,servings,already_have,cusine,budget,comments]
    cuisine_statement = ""
    for i in cusine:
        cuisine_statement += " ".join(cuisine_ingredients[i])
    prompt= f"""
    I need a grocery list for {duration} weeks, including {diet}. 
    I want to have {meals} every day, with each meal serving {servings} people. 
    I have {already_have} in my pantry. 
    I prefer the following cusines: {cuisine_statement}.
    {comments}
    Adjust the ingredient quantities based on my preferences and should last for the provided duration.
    I want a balanced meal plan and donot mind some leftovers.
    """

    sd = getter(prompt)
    print(sd)
    shopping_dict = ast.literal_eval(sd.split('=')[1].strip().split("print")[0].strip().split("`")[0])
    
    store_costs =  [sum(price for item, price in shopping_dict[i]) for i in shopping_dict] 
    total_cost = sum(store_costs)
    for n,i in enumerate(shopping_dict):
        st.subheader(f"{i} - ${store_costs[n]:.2f}")
        for item,price in shopping_dict[i]:
            st.write(f"{item} - ${price}")

    st.subheader(f"Total Cost: ${total_cost:.2f}")

    with open('shopping_list.json', 'w') as file:
            for i,j in shopping_list_memory.items():
                j[2]=""
            shopping_list_memory.update({time.ctime():[shopping_dict,list_data,"curr"]})
            json.dump(shopping_list_memory, file, indent=4)
