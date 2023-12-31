import streamlit
streamlit.title("My parents new healthy dinner")
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


import pandas as pd
my_fruit_list = pd.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avacado', 'Strawberries'])

streamlit.dataframe(my_fruit_list)

