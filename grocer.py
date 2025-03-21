import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
from grocery_list.ing import cuisine_ingredients
import time
import json

st.title("Todo-dumm")
st.subheader("Let's get your fridge filled!")
st.caption("I will help you generate the most optimizied grocery list for your next trip to the market!")


# md = Groq(id="deepseek-r1-distill-llama-70b")
md = Gemini(id="gemini-2.0-flash")
grocery_list_agent =Agent(
    description="You are a professional shopper and chef. You will help user with creating a grocery list to buy items from specified stores and fit within the given budget.",
    model = md,
    name = "Shopper",
    instructions=[
        "You are a highly efficient and knowledgeable grocery list generator.",
        "Your task is to create a shopping list for the user based on user preferences.",
        "you will get information from the stores specified by the user.",
        "You will see to it that the ingredients are matching any dietary preferences provided.",
        "You will add quantity for the user to buy and also suggest some meals that can be made with the items",
         "Your role is get prices for all the ingredients based on the quantity  and present in a tabulated format ",
         "The duration is specified in the prompt for you.",
        "Get ingredient information and prices from Raplhs, Target and Trader joes.",
        "you can add or remove ingredients as well from the given list",
        "the final output should be a table with ingredient name, quantity to buy, prices from all 3 store, best price to be used for out list in the final cost with it's quantity and store name",
        "The output size should be less than 6000 words.",
        "Use the tool to get recent prices.",
    ]
    , 
    tools=[ExaTools(api_key= "de8ed4f8-7cd1-4be0-8e2b-7d9beeb7f21b")]
)

# duration=input("Enter Duration in weeks: ")
# diet = input("Enter dietary preferences/ protien: ")
# meals =input("Enter meals (lunch/breakfast/dinner): ")
# servings = input("Enter no. of servings per meal : ")
# already_have = input("Any ingredients that you already have with quantity ? ")
# cusine = input("Cuisine Preference: ")
# comments = input("Additional comments that you want to add : ")
# budget = input(f"Enter your total budget for {duration} week duration : ")

# prompt= f"""
# I need a grocery list for {duration} weeks, including {diet}. 
# I want to have {meals} every day, with each meal serving {servings} people. 
# I have {already_have} in my pantry. 
# I prefer {cusine} recipes but am open to others if necessary. 
# {comments}
# Adjust the ingredient quantities based on my preferences and should last for the provided duration.
# I want a balanced meal plan and donot mind some leftovers.
# """

prompt= f"""
I need a grocery list for 4 weeks, including vegetables, chicken and eggs. 
I want to have lunch, dinner and breakfast every day, with each meal serving 1 people. 
I have nothing in my pantry. 
I prefer indian, italian and chinese recipes but am open to others if necessary. 
Provide the quantity required for each ingredient as well.
Adjust the ingredient quantities based on my preferences and should last for the provided duration.
I want a balanced meal plan and donot mind some leftovers.
create me a grocery list to buy from ralphs, target and trader joes. 
The list should have the prices mentioned for the store and approximate budget of $120.
Make sure the total cost is as close to the budget. 
"""
with st.form("my_form"):
    submit = st.form_submit_button("Shop On!")
if submit:
    response = grocery_list_agent.run(prompt, stream=False)
    st.write(str(response.content))

# print("Grocery list generated")
# print("Estimating cost....")

# cost_estimator = Agent(
#     description="You are a grocery list cost estimator",
#     model = md,
#     name = "Trainer",
#     instructions=[
#        "You will get a grocery list as an input.",
#        "Ensure that the total cost of the list doesn't exceed the budget provided by user."
#        "Your role is get prices for all the ingredients based on the quantity  and present in a tabulated format ",
#        "The duration is specified in the prompt for you.",
#        "Get ingredient information and prices from Raplhs, Target and Trader joes.",
#        "Finally provide total estimate cost, quantity and stores for each ingredient",
#        "you can add or remove ingredients as well from the given list",
#        "In the output, add prices from all 3 stores, and use the best price for total cost. total cost should include quantity "
#        "Ensure output is less than 6000 words and in a list format. also final output price should include quantity."
#     ]
#     , 
#     tools=[ExaTools(api_key= "de8ed4f8-7cd1-4be0-8e2b-7d9beeb7f21b")]
#     )
# prompt = response.content + f" Bugdet : $120"

# response1 = cost_estimator.run(prompt,stream=False)
# print(response1.content)