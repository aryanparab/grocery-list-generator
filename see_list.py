import streamlit as st
from  datetime import datetime
import mongo

from print_list import print_list




def convert(date_time):
    format = '%a %b %d %H:%M:%S %Y'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str



    

st.title("Hermes' List🧾")
st.subheader("Your Current shopping list")

if st.session_state['connected']:

    email = st.session_state['user_info'].get('email')
    my_lists = mongo.fetch_lists(email)
    if my_lists=="No Data Available":
         st.error("No Data Available")
    else:
        get_recent =  sorted([[i,convert(i['time'])] for i in my_lists],key=lambda x: x[1],reverse=True)
        to_show = get_recent[0][0]
        with st.form("other_lists"):
            your_lists = st.selectbox("Veiw Previous Lists? ",options=[i[0]['time'] for i in get_recent])
            submit = st.form_submit_button("View")
            if submit:
                to_show = [ i[0] for i in get_recent if i[0]['time']==your_lists][0]


        print_list([0,to_show['grocery_list'],to_show['time'],0],is_see_list=True)

else:
    st.error("Please Login")
