import streamlit as st

st.title("AI Elite Streamlit Demo")

st.header("Session for Elite-18")

st.subheader("by Lakshmi Teja")

name = st.text_input("Please enter your name:")

st.write(f"Hello, {name}! Welcome to the session")

course = st.radio("Select your course",['Data Analysis','Data Science','Full Stack'])

no_of_months = st.number_input("How many months would you like to dedicate for completing the course?")

st.write(f"You have opted for {course}. You decided to complete the course in {no_of_months} months time period.")

ratings = st.slider(f"Choose your ratings for the {course}",min_value=1.0,max_value=5.0,step=0.5,)

st.write(f"You have given {ratings} rating to the course")

if course == "Data Analysis":
    st.write("You have 4 months to complete the course")
elif course == "Data Science":
    st.write("You have 9 months to complete the course")

st.image(r"https://r1.ilikewallpaper.net/ipad-pro-wallpapers/download/91346/sea-sky-clouds-nature-sunset-4k-ipad-pro-wallpaper-ilikewallpaper_com_200.jpg")

st.sidebar.title("Select a page")

st.line_chart(data=[1,3,4,2,5,6,9,8])

st.code("a = input('Enter a name')")

st.latex(r'''
         ar + ar ^ 2 + ar ^ 3 + \cdots + ar ^ n-1 + ar ^ n = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right) )
         ''')
