import streamlit as st
st.title("Practical_day_2_ML_APP")
my_text=st.text("Hola que tal")
my_button = st.button("Run mL computation")

if my_button:
    st.title("The model is running now...")
#st.markdown("")
