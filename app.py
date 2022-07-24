import streamlit as st
string = "Odd-Even Finder"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Odd-Even Finder')
x = st.number_input('Enter a number')
if (x).is_integer():
    if x%2==0:st.write("your number is even")
    elif x%2!=0:st.write("your number is odd")
else:st.write("please enter integer number")
