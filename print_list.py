import streamlit as st


def toggle_item(key_value):
    st.session_state.grocery_status[key_value] = not st.session_state.grocery_status[key_value]

def print_list(val,is_see_list):
    _,shopping_dict , tim,_ = val
    weeks = list(shopping_dict.keys())
    week_totals = []
    target_list = []
    ralph_list =[]
    tj_list = []
    if 'grocery_status' not in st.session_state:
        st.session_state.grocery_status = {}
    
    st.caption(tim)
    for value in weeks:
        stores = shopping_dict[value]
        week_tots = 0
        st.subheader(value)
        for store in stores:
            tots = sum([i[1] for i in stores[store]])
            st.subheader(f"{store} - ${tots:.2f}")
            
            for n,product in enumerate(stores[store]):
                st.write(f"{n+1}. {product[0]} - $ {product[1]}")
            if store == "Target":
                target_list.append(tots)
            if store == "Ralphs":
                ralph_list.append(tots)
            if store == "Trader Joe's":
                tj_list.append(tots)
            week_tots = week_tots + tots

        st.subheader(f"{value} Total : {week_tots:.2f}")
        week_totals.append(week_tots)

    st.subheader(f"Total Cost: ${sum(week_totals):.2f}")



      
      

