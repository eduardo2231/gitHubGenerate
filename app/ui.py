import streamlit as st

import app

def main():
    st.write(
        """StackAI é uma ferramenta com inteligência artificial
    que gera badges profissionais no estilo GitHub a partir
    do nome de qualquer tecnologia, facilitando a criação
    de READMEs e portfólios.""")

    # Sua API key pegue em -------> https://aistudio.google.com/prompts/new_chat
    # Coloque dentro do arquivo app/.streamlit/secrets.toml dessa maneira -------> GEMINI_API_KEY = 'sua api_key'
    api_key = st.secrets["GEMINI_API_KEY"]

    try:
        text = app.app("eduardo", api_key)
        print(text)
    except NoneType as e:
        print(e)


if __name__ == '__main__':
    main()

