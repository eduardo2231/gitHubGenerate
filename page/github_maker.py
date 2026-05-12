import streamlit as st
from streamlit_sortables import sort_items

class MainGithub:
    def __init__(self):
        st.session_state.tech = {}

    def render(self):
        selectio_box()

#select box inicial
def selectio_box():
    with st.expander("README CREATE (WIP)", expanded=True):
        st.write("Aqui você configura e monta o conteúdo do seu README do GitHub, como apresentação, tecnologias, projetos e outras informações do seu perfil.")

        with st.expander("Sobre"):
            st.write(" Uma breve descrição sobre você (quem é e o que faz). Áreas que você gosta (ex: backend, IA, games, etc.).")

            result = persistent_button(
                key="abt_btn",
                label="Adicionar Sobre",
                value="valor gerado"
            )

            if result:
                st.write(st.session_state.items)

        with st.expander("Tecnologias"):
            st.write("Linguagens, frameworks e ferramentas que você usa.")

            result= persistent_button(
                key="tec_btn",
                label="Adicionar Tecnologias",
                value="valor gerado"
            )

            if result:
                st.write(st.session_state.items)

        with st.expander("Projetos"):
            st.write("Links ou destaques de projetos importantes.")

            result = persistent_button(
                key="prj_btn",
                label="Adicionar Projetos",
                value="valor gerado"
            )

            if result:
                st.write(st.session_state.items)

        with st.expander("Estatisticas"):
            st.write("Cards com dados do GitHub, como commits e linguagens mais usadas.")

            result = persistent_button(
                key="est_btn",
                label="Adicionar Estatisticas",
                value="valor gerado"
            )
            if result:
                st.write(st.session_state.items)

        with st.expander("Contatos"):
            st.write("Email, LinkedIn, Discord ou outras formas de te encontrar.")

            result = persistent_button(
                key="cnt_btn",
                label="Adicionar Contatos",
                value="valor gerado"
            )
            if result:
                st.write(st.session_state.items)

        with st.expander("Objetivo profissional"):
            st.write("O que você está buscando (emprego, estágio, aprendizado).")

            result = persistent_button(
                key="obp_btn",
                label="Adicionar Objetivo profissional",
                value="valor gerado"
            )
            if result:
                st.write(st.session_state.items)

        with st.expander("Extras visuais"):
            st.write("Badges, GIFs ou layout estilizado para deixar mais apresentável.")

            result = persistent_button(
                key="extra_btn",
                label="Adicionar Extras visuais",
                value="Extras visuais"
            )
            if result:
                st.write(st.session_state.items)

def persistent_button(key, label, value):
    if key not in st.session_state:
        st.session_state[key] = False

    if st.button(label):
        st.session_state[key] = True

    return st.session_state[key]

