import streamlit as st

class Sidebar:

    def __init__(self):
        self.githubmaker = None
        self.badges_maker = None

    def render(self):
        with st.sidebar:
            st.markdown("""
            Se esse app te ajudou ou achou interessante, considere apoiar acompanhando meus projetos e conexões. Sempre estou criando coisas novas envolvendo Python, IA, dados e automações.

            🔗 [LinkedIn](https://www.linkedin.com/in/eduardo-bonometti-30572a34a/)  💻 [GitHub](https://github.com/eduardo2231)
            """)
