from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
import streamlit as st


def getter(prompt):
    with open("small_database.txt","r") as file:
        small_db = file.read()

    md = Gemini(id="gemini-2.0-flash")
    # md = Groq(id="deepseek-r1-distill-llama-70b")
    grocery_list_agent =Agent(
        description="You are a professional shopper and chef. You will help user with creating a grocery list to buy items from specified stores and fit within the given budget.",
        model = md,
        name = "Shopper",
        instructions=[
        "You will create a grocery list from specified ingredients and their quantities and a prompt as an input.",  
    "Retrieve ingredient information and prices from Ralphs, Target, and Trader Joe’s.",  
    "Provide prices for each ingredient from all three stores.",  
    """Present the results in a clear, tabulated format with columns for:  
        - Ingredient,  
        - Quantity,  
        - Price at Ralphs,  
        - Price at Target,  
        - Price at Trader Joe’s,  
        - Total Cost (Including Quantity).""",  
    "You are allowed to add or remove ingredients from the given list if necessary for availability or cost-effectiveness.",  
    "Provide a total estimated cost for all ingredients, considering the specified quantities.",  
    "Ensure the output remains concise and clear, with a maximum length of 6000 words.",  
    "Ensure the final output includes the store-specific prices and the total cost reflecting the required quantities.",  
    "The output should be in a clean list format for easy reference.",  
    "Use the following information for price reference ( this is real time data)",
    small_db,"If you can't find the required prices here, use the exa toll provided."

        ]
        , 
        tools=[ExaTools(api_key= "de8ed4f8-7cd1-4be0-8e2b-7d9beeb7f21b")]
    )

    # prompt= f"""
    # I need a grocery list for 4 weeks, including vegetables, chicken and eggs. 
    # I want to have lunch, dinner and breakfast every day, with each meal serving 1 people. 
    # I have nothing in my pantry. 
    # I prefer {cuisine_ingredients['Indian']}, {cuisine_ingredients['Italian']} recipes but am open to others if necessary. 
    # Provide the quantity required for each ingredient as well.
    # Adjust the ingredient quantities based on my preferences and should last for the provided duration.
    # I want a balanced meal plan and donot mind some leftovers.
    # create me a grocery list to buy from ralphs, target and trader joes. 
    # The list should have the prices mentioned for the store and approximate budget of $120.
    # Make sure the total cost is as close to the budget. 
    # only output the ingredients and their quantity required
    # """

    # cost_estimator = Agent(
    #     description="You are a grocery list cost estimator",
    #     model = md,
    #     name = "Cost estimator",
    #     instructions=[
    #             "You will receive a grocery shopping list as input.",  
    # "Create a to-do list along with the prices for the items.",  
    # "For each ingredient, provide the prices from Ralphs, Target, and Trader Joe’s.",  
    # "Add the total price at the end, reflecting the best choices for each store.",  
    # "Ensure you select the best price for each ingredient across all three stores.",  
    # "Distribute the items among different stores instead of purchasing everything from one store.",  
    # "Make sure the total cost is within $15 of the $120 budget (between $105 and $135).",  
    # "Adjust the list by adding or removing items to meet the budget as accurately as possible.",  
    # "Present the results in a clear and organized format, divided by stores indicating where each item should be bought.",  
    #     ]
    #     , 
    #     tools=[ExaTools(api_key= "de8ed4f8-7cd1-4be0-8e2b-7d9beeb7f21b")]
    #     )
    

    to_creator = Agent(
        description="You are a to do list generatot",
        model = md,
        name = "List generator",
        instructions=[
        "You will receive a grocery list with specified ingredients and their quantities as input.",  
"Generate a grocery list for each store (Trader Joe's, Target, and Ralphs).",  
"Organize the output into a dictionary format with the store names as keys and the items as lists of tuples.",  
"Each tuple should contain the item name (as a string) and the price (as a float, reflecting the cost per specified quantity).",  
"Present the output in the following format always!:",  
"grocery_data = {",  
"    'Trader Joe\'s': [",  
"        ('Chicken Breast (3 lbs)', 21.00),",  
"        ('Eggs (24)', 5.00),",  
"        ('Lentils (Toor/Masoor) (2 lbs)', 6.00),",  
"        # More items",  
"    ],",  
"    'Target': [",  
"        ('Paneer (Low-Fat) (1 lb)', 7.00),",  
"        ('Bell Peppers (3)', 4.50),",  
"        # More items",  
"    ],",  
"    'Ralphs': [",  
"        ('Avocado (2)', 4.00),",  
"        # More items",  
"    ]",  
"}",  
"For each ingredient, find the best price from the available stores and choose it.",  
"Distribute items across the stores, ensuring that not all items are bought from a single store.",  
"Ensure the list is balanced and doesn’t exceed the expected budget for each store. Make this top priority It is okay to be + or - $15 of the total value",  
"Maintain the specified quantities and ingredients consistently across all stores.",  
"Output the list in the exact format shown above with each item and its cost correctly aligned."


        ]
    )

    

    with st.status("Generating List...", expanded=True) as status:
        response = grocery_list_agent.run(prompt, stream=False)
        st.write("Estimating cost....")
        # prompt = response.content + " Use the following list to estimate the cost of items from provided stores"
        # response = cost_estimator.run(prompt,stream=False)
        st.write("Creating List")
        prompt = response.content + " Create a to-do list for the list of grocery items to buy."
        response2 = to_creator.run(prompt,stream=False)
        status.update(
        label="List Generation complete!", state="complete", expanded=False
        )

    return str(response2.content)