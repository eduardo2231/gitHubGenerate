from app.ui import main
import streamlit as st

if __name__ == '__main__':
    api_key = st.secrets["GEMINI_API_KEY"]
    main(api_key)
