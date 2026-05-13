from page.badges_maker import MainBadge
import streamlit as st
from app.sidebar import Sidebar

if __name__ == "__main__":
    sidebar = Sidebar()
    page = sidebar.render()
    MainBadge()