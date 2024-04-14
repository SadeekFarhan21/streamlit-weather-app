import streamlit as st

st.title('Farhan')
temperature, wind, direction = st.columns(3)

temp = 20
speed = 45
common_dir = 'North'



with temperature:
    st.subheader(f'{temp} °F')
    st.write('Temperature')
with wind:
    st.subheader(f'{speed} MPH')
    st.write('Wind Speed')
with direction:
    st.subheader(f'{common_dir}')
    st.write('Wind Direction')
    