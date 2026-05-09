import streamlit as st
from app.badge import generate_badges
from app.badge import is_valid_badge

def main(api: str):
    st.title("StackAI")
    st.write(
        """StackAI é uma ferramenta com inteligência artificial
    que gera badges profissionais no estilo GitHub a partir
    do nome de qualquer tecnologia, facilitando a criação
    de READMEs e portfólios.""")
    # Sua API key pegue em -------> https://aistudio.google.com/prompts/new_chat
    # Coloque dentro do arquivo app/.streamlit/secrets.toml dessa maneira -------> GEMINI_API_KEY = 'sua api_key'

    tech = st.text_input("Digite as tecnologias (ex: Python, Docker, React):")
    if st.button("Gerar Badges"):
        if tech.strip() == "":
            st.warning("Por favor, digite ao menos uma tecnologia.")
        else:
            with st.spinner("Gerando badges..."):
                try:
                    result = generate_badges(tech, api)
                    st.success("Badges gerados!!")
                    st.markdown(result)
                    st.code(result, language="markdown")
                except Exception as e:
                    st.error(f"Erro ao gerar badge: {e}")
    st.write("""
    Depois de gerar suas badges, copie o código abaixo e cole no seu arquivo **README.md** do GitHub.
    Cada badge representa uma tecnologia usada no seu projeto e ajuda a deixar seu repositório mais profissional e organizado.
    Basta colar o Markdown gerado diretamente no README e ele será renderizado automaticamente como imagem no GitHub.
    """
    )
    st.markdown("[Acesse o meu GitHub](https://github.com/eduardo2231)")
    st.image("app/exemple.png")
    st.image("app/exemple2.png")

