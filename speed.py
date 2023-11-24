# app.py
import streamlit as st

st.markdown("<h1 style='text-align: center; color: #0000FF;'>Speed Limit Detection</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size:22px;'>This is a app that detect the speed limit</p>", unsafe_allow_html=True)

# Add a text input
user_input = st.number_input("Enter the Speed:", min_value=0, max_value=None, value=0, step=1)

# Display the input

selected_option = st.selectbox("Select an Area:", ["Urban Area", "Rural Area", "Highways"])
st.write("You are travelling ", user_input, "at", selected_option)

if selected_option == "Urban Area":
    if user_input > 40:
        st.markdown("<div style='display: flex; justify-content: center;'>"
                        "<img src='https://upload.wikimedia.org/wikipedia/commons/1/17/Warning.svg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size:22px;'>You have exceeded the speed limit of 40km/h !!!!!!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='display: flex; justify-content: center; height: 200px; width: 80%; background-color: None;'>"
                        "<img src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*lpWX1QftoVYDZDYdsGhEtg.jpeg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='font-size:22px; text-indent: 40px;'>You have not exceeded the speed limit of 40km/h !!!!!!</p>", unsafe_allow_html=True)

if selected_option == "Rural Area":
    if user_input > 80:
        st.markdown("<div style='display: flex; justify-content: center;'>"
                        "<img src='https://upload.wikimedia.org/wikipedia/commons/1/17/Warning.svg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size:22px;'>You have exceeded the speed limit of 80km/h !!!!!!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='display: flex; justify-content: center; height: 200px; width: 80%; background-color: None;'>"
                        "<img src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*lpWX1QftoVYDZDYdsGhEtg.jpeg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='font-size:22px; text-indent: 40px;'>You have not exceeded the speed limit of 80km/h !!!!!!</p>", unsafe_allow_html=True)


if selected_option == "Highways":
    if user_input > 120:
        st.markdown("<div style='display: flex; justify-content: center;'>"
                        "<img src='https://upload.wikimedia.org/wikipedia/commons/1/17/Warning.svg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size:22px;'>You have exceeded the speed limit of 120km/h !!!!!!</p>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='display: flex; justify-content: center; height: 200px; width: 80%; background-color: None;'>"
                        "<img src='https://miro.medium.com/v2/resize:fit:720/format:webp/1*lpWX1QftoVYDZDYdsGhEtg.jpeg' alt='Warning Image'></div>",
                        unsafe_allow_html=True)
        st.markdown("<p style='font-size:22px; text-indent: 40px;'>You have not exceeded the speed limit of 120km/h !!!!!!</p>", unsafe_allow_html=True)

