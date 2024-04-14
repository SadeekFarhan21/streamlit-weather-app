import streamlit as st

def main():
    st.title("Map in Streamlit")

    # Display a map centered on a specific location
    st.map([40.7128, -74.0060], zoom=10)

if __name__ == "__main__":
    main()
