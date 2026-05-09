import streamlit as st
import app

def main():
    st.title("StackAI")
    st.write(
        """StackAI é uma ferramenta com inteligência artificial
    que gera badges profissionais no estilo GitHub a partir
    do nome de qualquer tecnologia, facilitando a criação
    de READMEs e portfólios.""")
    # Sua API key pegue em -------> https://aistudio.google.com/prompts/new_chat
    # Coloque dentro do arquivo app/.streamlit/secrets.toml dessa maneira -------> GEMINI_API_KEY = 'sua api_key'
    api_key = st.secrets["GEMINI_API_KEY"]

    tech = st.text_input("Digite as tecnologias (ex: Python, Docker, React):")
    if st.button("Gerar Badges"):
        if tech.strip() == "":
            st.warning("Por favor, digite ao menos uma tecnologia.")
        else:
            with st.spinner("Gerando badges..."):
                try:
                    result = app.app(tech, api_key)
                    st.success("Badges gerados!")
                    st.markdown(result)
                    st.code(result, language="markdown")
                except Exception as e:
                    st.error(f"Erro ao gerar badges: {e}")


