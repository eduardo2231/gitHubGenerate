import streamlit as st
from app.ai.badge_ai import generate_badges, generate_stats
import streamlit.components.v1 as components


def MainBadge(api=st.secrets["GROQ_API_KEY"]):

    tab1, tab2 = st.tabs(["🧩 Badges", "📊 GitHub Stats"])

    # =========================
    # TAB 1 - BADGES
    # =========================
    with tab1:
        tech = st.text_input("Digite as tecnologias (ex: Python, Docker, React):")
        style_options = ['for-the-badge', 'flat']
        style = st.selectbox('Escolha um style:', style_options)

        if tech:
            st.write('Selecionadas:', tech)

        if st.button("Gerar Badges"):
            if tech.strip() == "":
                st.warning("Por favor, digite ao menos uma tecnologia.")
            else:
                with st.spinner("Gerando badges..."):
                    try:
                        result = generate_badges(tech, api, style)
                        st.success("Badges gerados!!")
                        st.code(result, language="markdown")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Erro ao gerar: {e}")

    # =========================
    # TAB 2 - STATS
    # =========================
    with tab2:
        user = st.text_input("Digite seu username:")
        stats_options = [
            'SPLIT DASHBOARD STYLE',
            'HERO HEADER STYLE',
            'MINIMAL DEVELOPER STYLE',
            'CYBER NEON STYLE',
            'DATA DASHBOARD STYLE'
        ]

        stats = st.selectbox('Escolha um style:', stats_options)
        if user:
            st.write('Username:', user)
        if st.button("Gerar stats"):
            if user.strip() == "":
                st.warning("Por favor, digite seu username.")
            else:
                with st.spinner("Gerando..."):
                    try:
                        result = generate_stats(user, api, stats)
                        st.success("Stats gerados!!")
                        st.code(result, language="markdown")
                        st.subheader("Preview do README")

                        components.html(
                            result,
                            height=400,
                            scrolling=True
                        )
                    except Exception as e:
                        st.error(f"Erro ao gerar: {e}")
    st.write("""
    Depois de gerar o código, copie todo o conteúdo exibido na saída e cole diretamente no arquivo README.md do seu repositório no GitHub.
    O GitHub interpreta automaticamente o README.md como um arquivo Markdown, então tudo o que estiver no formato correto será renderizado
    na página do repositório assim que você fizer o commit.
       """
             )
    st.image("app/assets/example.png")

