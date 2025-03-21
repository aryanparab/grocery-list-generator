from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.exa import ExaTools
from ing import cuisine_ingredients

md = Gemini(id="gemini-2.0-flash")
string_items = [f"{key}: {value}" for key, value in cuisine_ingredients.items()]
my_string = ", ".join(string_items)
# md = Groq(id="deepseek-r1-distill-llama-70b")
grocery_list_agent =Agent(
        description="You are a database creator. You need to create a database for ingredients used in different cuisines and maintain real time prices.",
        model = md,
        name = "Shopper",
        instructions=[
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
    "Ensure the output remains concise and clear, with a maximum length of 6000 words.",  
    "Ensure the final output includes the store-specific prices and the total cost reflecting the required quantities.",  
    "Ensure all prices are real time and accurately taken from exatools",

        ]
        , 
        tools=[ExaTools(api_key= "de8ed4f8-7cd1-4be0-8e2b-7d9beeb7f21b")]
    )

prompt = f"""
Retrieve real-time prices from Ralphs, Trader Joe's, and Target for grocery ingredients. 
Include prices for as many ingredients as possible that are commonly used for cooking a variety of cuisines, 
including to Indian, Chinese, American, Mexican, Mediterranean, Greek, Italian, Japanese, Thai, French, and Middle Eastern.
Ensure that ingredients for each cuisine is used
Instructions:

Get prices from all three stores — Ralphs, Trader Joe's, and Target.
Provide prices for standard quantities like 1 lb, 1 dozen, or 1 gallon as applicable.
Present the data in a clear tabulated format with columns for:
Ingredient
Quantity
Price at Ralphs
Price at Trader Joe's
Price at Target
Include foundational and commonly used ingredients such as:
Proteins (e.g., chicken breast, eggs, tofu, paneer, salmon)
Rice Varieties (e.g., basmati rice, jasmine rice, brown rice, wild rice)
Vegetables (e.g., tomatoes, onions, spinach, bell peppers, carrots)
Dairy (e.g., milk, yogurt, paneer, feta cheese, parmesan)
Grains (e.g., whole wheat flour, tortillas, pasta, oats)
Oils and Fats (e.g., olive oil, sesame oil, butter, ghee)
Legumes and Beans (e.g., lentils, black beans, chickpeas, kidney beans)
Fruits (e.g., lemons, avocados, bananas, apples)
Spices and Condiments (e.g., cumin, coriander, turmeric, soy sauce, vinegar)
Ensure the data is accurate and reflects the latest available prices.

First find the nescessary ingredients required for each cuisine and then fetch their prices in real time from the web.
some necessary ingredients based on cusines are: """ + my_string + """
Return the final data as a well-structured JSON or string in the following format:

{
  "store_name": [
    {"ingredient": "ingredient_name", "quantity": "1 lb", "price": 2.50},
    {"ingredient": "ingredient_name", "quantity": "1 dozen", "price": 5.00}
  ],
  "store_name": [
    {"ingredient": "ingredient_name", "quantity": "1 lb", "price": 3.00},
    {"ingredient": "ingredient_name", "quantity": "1 gallon", "price": 4.75}
  ]
}
Additional Notes:

Use efficient data storage to minimize unnecessary repetition.
Avoid duplicate or irrelevant data.
If any ingredient is unavailable, provide a clear indication.
The goal is to generate an optimized and accurate grocery price comparison for further analysis."""

print(prompt)
response = grocery_list_agent.run(prompt,stream=False)

with open('small_database.txt','w') as file:
    file.write(response.content)
