from google import genai
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
    client = genai.Client(api_key=api)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

    # for m in client.models.list():
        # print(m.name)

def is_valid_badge(text: str) -> bool:
    pattern = r"^!\[.+\]\(https://img\.shields\.io/badge/.+\)$"
    return bool(re.match(pattern.strip(), text.strip()))

#print(app("GitHub"))