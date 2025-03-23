from pymongo import MongoClient
import certifi

connection_string = "mongodb+srv://parabaryan:v7tG302WB2BoHyL7@cluster0.ysldz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string,tlsCAFile=certifi.where())

dbs = client.production
shopping = dbs.shopping
recipes = dbs.recipes

def insert_grocery_list(shopping_dict):
    shopping.insert_one({"email":shopping_dict[0],"time":shopping_dict[2],"grocery_list":shopping_dict[1],"prompt":shopping_dict[3]})


def fetch_lists(email):
    all_lists = [i for i in shopping.find({"email":email})]
    if all_lists ==[]:
        return "No Data Available"
    return all_lists

def fetch_recipes(email):
    all_recipes = [ i for i in recipes.find({"email":email})]
    if all_recipes == []:
        return "No Data Available"
    return all_recipes

def insert_recipes(email,recipe,tim,prompt):
    rr = fetch_recipes(email)
    if rr =="No Data Available":
        recipes.insert_one({"email":email,"recipe":recipe,"time":tim,"prompt":prompt})
    else:
        
        rr_for_date = [ i for i in rr if i["time"]==tim]
        if rr_for_date == []:
            recipes.insert_one({"email":email,"recipe":recipe,"time":tim,"prompt":prompt})
        else:
            recipes.update_one({"email":email,"time":tim},{"$set":{"recipe":recipe,"prompt":prompt}})
# production = client.production
# person_collection = production.person_collection

# def create_document():
#     first_names=["sjj","djsi","huais"]
#     last_names = ["shash","aus","ruesdak"]
#     ages =[ 23,232,12]
#     docs = []

#     for first_name,last_name,age in zip(first_names,last_names,ages):
#         doc = {"first name":first_name,"last name":last_name,"age":age}
#         docs.append(doc)
#     person_collection.insert_many(docs)
# #create_document()

# printer = pprint.PrettyPrinter()
# def find_all_people():
#     people = person_collection.find()
#     #print(list(people))
#     for person in people:
#         printer.pprint(person)
    
