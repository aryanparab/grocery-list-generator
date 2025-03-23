from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.exa import ExaTools


md = Gemini(id="gemini-2.0-flash")

# md = Groq(id="deepseek-r1-distill-llama-70b")
grocery_list_agent =Agent(
        description="You are a price finder. You need to fetch prices for ingredients used in different cuisines and maintain real time prices.",
        model = md,
        name = "Shopper",
        instructions=[
    "Retrieve ingredient information and prices from Ralphs, Target, and Trader Joe’s.",  
    "Provide prices for each ingredient from all three stores.",   
    "Ensure the output remains concise and clear, with a maximum length of 6000 words.",  
    "Ensure the final output includes the store-specific prices and the total cost reflecting the required quantities.",  
    "Ensure all prices are real time and accurately taken from exatools",
    "Output should be less than 6000 tokens"

        ]
        , 
        tools=[ExaTools(api_key= "3dcbca53-7254-4731-9b34-3948bc454191")]
    )
additional_data = ""
p1  = """
Retrieve real-time prices from Ralphs, Trader Joe's, and Target for grocery ingredients. 
Instructions:
Provide prices for standard quantities like 1 lb, 1 dozen, or 1 gallon as applicable.
Ingredient
Quantity
Price at Ralphs
Price at Trader Joe's
Price at Target
Include foundational and commonly used ingredients . Make sure to get data for all of the following:   """
p2 = """

Ensure the data is accurate and reflects the latest available prices.
First find the nescessary ingredients required for each cuisine and then fetch their prices in real time from the web.
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

ingredient_lists = [
    # List 1: Indian Cuisine Essentials
    [
        "Basmati Rice",
        "Whole Wheat Flour (Atta)",
        "Toor Dal",
        "Masoor Dal",
        "Moong Dal",
        "Chickpeas (Chana)",
        "Paneer",
        "Ghee",
        "Mustard Seeds",
        "Cumin Seeds",
        "Coriander Powder",
        "Turmeric Powder",
        "Garam Masala",
        "Red Chili Powder",
        "Asafoetida (Hing)",
        "Curry Leaves",
        "Tamarind Paste",
        "Coconut Milk",
        "Green Chilies",
        "Ginger",
    ],
    # List 2: More Indian and Some General Staples
    [
        "Garlic",
        "Onions",
        "Tomatoes",
        "Spinach",
        "Potatoes",
        "Eggplant",
        "Cauliflower",
        "Fresh Coriander (Cilantro)",
        "Yogurt",
        "Bay Leaves",
        "Cardamom Pods",
        "Cloves",
        "Jasmine Rice",
        "Rice Noodles",
        "Soy Sauce",
        "Oyster Sauce",
        "Hoisin Sauce",
        "Rice Vinegar",
        "Sesame Oil",
        "Shaoxing Wine",
    ],
    # List 3: Asian Cooking Ingredients
    [
        "Tofu",
        "Bok Choy",
        "Napa Cabbage",
        "Chinese Broccoli",
        "Ginger",
        "Garlic",
        "Green Onions",
        "Bean Sprouts",
        "Bell Peppers",
        "Carrots",
        "Snow Peas",
        "Shiitake Mushrooms",
        "Bamboo Shoots",
        "Water Chestnuts",
        "Chili Oil",
        "Five-Spice Powder",
        "White Pepper",
        "Star Anise",
        "Ground Pork",
        "Whole Duck",
    ],
    # List 4: Baking and General Pantry Items
    [
        "Egg Noodles",
        "Black Vinegar",
        "All-Purpose Flour",
        "Cornmeal",
        "Baking Powder",
        "Baking Soda",
        "Butter",
        "Eggs",
        "Milk",
        "Heavy Cream",
        "Cheddar Cheese",
        "Chicken Breast",
        "Ground Beef",
        "Bacon",
        "Hot Dogs",
        "Ketchup",
        "Mustard",
        "Barbecue Sauce",
        "Mayonnaise",
        "Ranch Dressing",
    ],
    # List 5: Bread, Sweeteners, and Produce
    [
        "White Bread",
        "Brown Sugar",
        "Maple Syrup",
        "Potatoes",
        "Corn",
        "Green Beans",
        "Lettuce",
        "Tomatoes",
        "Avocado",
        "Apple Cider Vinegar",
        "Macaroni Pasta",
        "Vegetable Oil",
        "Corn Tortillas",
        "Flour Tortillas",
        "Masa Harina",
        "Black Beans",
        "Pinto Beans",
        "Refried Beans",
        "Mexican Rice",
        "Avocados",
    ],
    # List 6: More Mexican Cuisine Ingredients
    [
        "Jalapeños",
        "Serrano Peppers",
        "Poblano Peppers",
        "Tomatillos",
        "Roma Tomatoes",
        "Onions",
        "Garlic",
        "Cilantro",
        "Limes",
        "Chipotle Peppers in Adobo",
        "Ancho Chilies",
        "Guajillo Chilies",
        "Queso Fresco",
        "Cotija Cheese",
        "Oaxaca Cheese",
        "Sour Cream (Crema)",
        "Chicken Thighs",
        "Ground Beef",
        "Chorizo",
        "Epazote",
    ],
    # List 7: Oils, Sauces, and More Mexican Staples
    [
        "Avocado Oil",
        "Mole Sauce",
        "Corn Husks",
        "Mexican Oregano",
        "Cinnamon (Canela)",
        "Bay Leaves",
        "Agave Syrup",
        "Olive Oil",
        "Red Wine Vinegar",
        "Lemons",
        "Garlic",
        "Onions",
        "Tomatoes",
        "Cucumber",
        "Bell Peppers",
        "Eggplant",
        "Zucchini",
        "Feta Cheese",
        "Halloumi Cheese",
        "Greek Yogurt",
    ],
    # List 8: Mediterranean and Greek Ingredients
    [
        "Hummus",
        "Tahini",
        "Pita Bread",
        "Lentils",
        "Chickpeas",
        "Fresh Parsley",
        "Fresh Mint",
        "Kalamata Olives",
        "Capers",
        "Orzo Pasta",
        "Bulgur Wheat",
        "Rice",
        "Ground Lamb",
        "Chicken Breast",
        "Sardines",
        "Anchovies",
        "Paprika",
        "Olive Oil",
        "Lemon Juice",
        "Garlic",
    ],
    # List 9: More Mediterranean Flavors
    [
        "Onions",
        "Tomatoes",
        "Cucumbers",
        "Bell Peppers",
        "Oregano",
        "Dill",
        "Mint",
        "Parsley",
        "Feta Cheese",
        "Kalamata Olives",
        "Greek Yogurt",
        "Pita Bread",
        "Phyllo Dough",
        "Honey",
        "Rice",
        "Bulgur Wheat",
        "Lentils",
        "Chickpeas",
        "Lamb",
        "Chicken Thighs",
    ],
    # List 10: European Cuisine Staples
    [
        "White Fish Fillets",
        "Eggplant",
        "Zucchini",
        "Spinach",
        "Red Wine Vinegar",
        "Cinnamon",
        "Nutmeg",
        "Olive Oil",
        "Garlic",
        "Onions",
        "Basil",
        "Oregano",
        "Thyme",
        "Parsley",
        "Rosemary",
        "Tomatoes",
        "Tomato Paste",
        "Parmesan Cheese",
        "Mozzarella Cheese",
        "Ricotta Cheese",
    ],
    # List 11: Italian Cuisine Ingredients
    [
        "Pasta (Spaghetti, Penne, Fettuccine)",
        "Arborio Rice",
        "Prosciutto",
        "Italian Sausage",
        "Ground Beef",
        "Chicken Breast",
        "Red Wine",
        "Balsamic Vinegar",
        "Capers",
        "Artichokes",
        "Eggplant",
        "Zucchini",
        "Bell Peppers",
        "Cannellini Beans",
        "Pine Nuts",
        "Bread Flour",
        "Basil Pesto",
        "Jasmine Rice",
        "Sticky Rice",
        "Rice Noodles",
    ],
    # List 12: Thai Cuisine Ingredients
    [
        "Coconut Milk",
        "Fish Sauce",
        "Soy Sauce",
        "Oyster Sauce",
        "Thai Chili Paste",
        "Thai Green Curry Paste",
        "Thai Red Curry Paste",
        "Lemongrass",
        "Galangal",
        "Kaffir Lime Leaves",
        "Thai Basil",
        "Cilantro",
        "Green Onions",
        "Garlic",
        "Shallots",
        "Bird’s Eye Chilies",
        "Tamarind Paste",
        "Palm Sugar",
        "Limes",
        "Bean Sprouts",
    ],
    # List 13: More Thai and Japanese Ingredients
    [
        "Peanuts",
        "Coconut Sugar",
        "Tofu",
        "Ground Pork",
        "Chicken Breast",
        "Shrimp",
        "Cashew Nuts",
        "Eggplant",
        "Bamboo Shoots",
        "Water Spinach",
        "Carrots",
        "Cucumber",
        "Short-Grain Rice",
        "Nori",
        "Miso Paste",
        "Soy Sauce",
        "Mirin",
        "Sake",
        "Rice Vinegar",
        "Dashi",
    ],
    # List 14: Japanese Cuisine Ingredients
    [
        "Bonito Flakes",
        "Kombu",
        "Tofu",
        "Shiitake Mushrooms",
        "Enoki Mushrooms",
        "White Radish",
        "Green Onions",
        "Bok Choy",
        "Spinach",
        "Nappa Cabbage",
        "Edamame",
        "Wasabi",
        "Pickled Ginger",
        "Ramen Noodles",
        "Udon Noodles",
        "Soba Noodles",
        "Matcha",
        "Japanese Mayonnaise",
        "Furikake",
        "Wakame",
    ],
    # List 15: Fish and General Ingredients
    [
        "Fish Roe",
        "Salmon",
        "Tuna",
        "Eel",
        "Tempura Flour",
        "Panko Breadcrumbs",
        "Katsu Sauce",
        "Fruits (e.g., lemons, avocados, bananas, apples)",
    ],
]

final  =""
for i in ingredient_lists:
    prompt = p1+" ".join(i) + p2
    response = grocery_list_agent.run(prompt,stream=False)
    final = final + str(response.content)

with open('small_database.txt','w') as file:
    file.write(final)
