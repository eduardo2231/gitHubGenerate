from page.badges_maker import MainBadge
from page.github_maker import MainGithub
import streamlit as st
from app.sidebar import Sidebar

def main_dashboard():
    # renderizando a barra lateral
    sidebar = Sidebar()
    page = sidebar.render()

    # paginas
    if page == "badges":
        MainBadge()

    elif page == "github":
        github = MainGithub()
        github.render()


if __name__ == "__main__":
    main_dashboard()
