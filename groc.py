
from ing import cuisine_ingredients
from shopper import getter
import streamlit as st
import time
from mongo import insert_grocery_list
import ast
from print_list import print_list



st.title("Hermes' List🧾")
st.subheader("Let's get your fridge filled!👨‍🌾👨🏻‍🍳")
st.caption("I will help you generate the most optimizied grocery list for your next trip to the market!🛒")


cuisines = list(cuisine_ingredients.keys())

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

if st.session_state['connected']:

    if submit :
        
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
        Provide a grocery list in the budget of ${budget}.
        Ensure all the budget is used for the ingredients. It is okay to okay over budget by $15
        Adjust the ingredient quantities based on my preferences and should last for the provided duration.
        I want a balanced meal plan and donot mind some leftovers.
        """
        prompt_to_save = {
            "duration":duration,
            "budget":budget,
            "cuisines":cusine,
            "diet":diet,
            "servings":servings,
            "meals":meals,
            "comments":comments,
            "already_have":already_have
        }
        while True:
            try:
                output = getter(prompt)
                shopping_dict = ast.literal_eval(output.split('=')[1].strip().split("print")[0].strip().split("`")[0].strip())
                if shopping_dict:
                    break
            except:
                st.info("Reoptimizing List")
        
        val = [st.session_state['user_info'].get('email'),shopping_dict,time.ctime(),prompt_to_save]
        print_list(val,False)
        
        insert_grocery_list(val)
       
else:
    st.subheader("Please Login!!")
