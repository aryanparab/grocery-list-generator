from ing import cuisine_ingredients
from chef import cooker
import streamlit as st
from datetime import datetime
import mongo



st.title("Hermes' List🧾")
st.subheader("Create a Meal Plan🍳🗓️")
st.caption("Let's create a meal plan based on your grocery list👨🏻‍💻")


def convert(date_time):
    format = '%a %b %d %H:%M:%S %Y'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str


if st.session_state['connected']:
    email = st.session_state['user_info'].get('email')
    my_lists = mongo.fetch_lists(email)
    if my_lists=="No Data Available":
         st.error("No Data Available")
    else:
        get_recent =  sorted([[i,convert(i['time'])] for i in my_lists],key=lambda x: x[1],reverse=True)
        to_show = get_recent[0][0]['prompt']
        
        recipes = mongo.fetch_recipes(email)
        
        time_to_see = get_recent[0][0]['time']
        with st.form("other_lists"):
            your_lists = st.selectbox("Veiw Previous Recipes? ",options=[i[0]['time'] for i in get_recent])
            submit = st.form_submit_button("View")
            if submit:
                time_to_see = your_lists
            
        if recipes == "No Data Available":
            recipe = ""
        else:
            recipe =[ i for i in recipes if str(i['time'])==time_to_see]
            get_recent_here = [i for i in my_lists if i['time']==time_to_see]
            to_show  = get_recent_here[0]['prompt']
            if recipe ==[]:
                recipe=""
            else:
                recipe =[ i for i in recipes if str(i['time'])==time_to_see][0]['recipe']

        statement =f"""
        The recipes displayed are for a duration of {to_show['duration']} weeks. They include the following - {",".join(to_show['diet'])}.
        You will be provided recipes for : {",".join(to_show['meals'])}. No: of servings per meal : {to_show['servings']}.
        Your selected cuisine preferences are : {",".join(to_show['cuisines'])}. 
        comments you would like to add : {to_show['comments']}
        """

        prompt = st.text_area(value=statement,label="",height=150)
        gen = st.button("Generate new?")


        if gen:
            new_rec = cooker(prompt+"  Grocery list : " + str(get_recent[0][0]['grocery_list']))
            st.caption(time_to_see)
            st.write(new_rec)
            mongo.insert_recipes(email,new_rec,time_to_see,prompt)
        else:
            st.caption(time_to_see)
            st.write(recipe)
else:
    st.error("Please Login")