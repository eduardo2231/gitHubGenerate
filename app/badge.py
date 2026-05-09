# from google import genai
from groq import Groq
import streamlit as st
import re

def generate_badges(tech: str, api: str) -> str:

    prompt = f'''Generate only GitHub-style Markdown badges using Shields.io.
    Rules:
    Output ONLY badges (no explanations, no text, no titles)
    Each item must follow this format: 
    Return only valid Markdown lines
    Do not include code blocks
    Do not include comments or extra formatting
    Use correct official logos from Simple Icons
    Choose appropriate colors for each technology
    If unsure about color, pick a standard official brand color
    Technologies will be provided by the user
    Input:
    {tech}
    Output:
    ONLY badges in Markdown format and only test ordered in 'Input:
    {tech}' '''
    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        )

    return response.choices[0].message.content

    # for m in client.models.list():
        # print(m.name)

# not using
def is_valid_badge(text: str) -> bool:
    pattern = r"^!\[.+\]\(https://img\.shields\.io/badge/.+\)$"
    return bool(re.match(pattern.strip(), text.strip()))

#print(app("GitHub"))