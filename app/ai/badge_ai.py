# from google import genai
from groq import Groq
import streamlit as st
import re

def generate_badges(tech: str, api: str, style) -> str:

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
    {tech}' and which following style {style}, if dont exists, use the standard style flat'''
    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
        )

    return response.choices[0].message.content

    # for m in client.models.list():
        # print(m.name)

    # style=for-the-ai
    # style=flat

def generate_stats(user: str, api: str, style) -> str:
    prompt = f'''You are a GitHub README generator. Output ONLY raw Markdown — no explanations, no code fences, no comments.

## Inputs
- `{user}` — GitHub username
- `{style}` — Layout style (1–5, see below)

## Rules
- All image URLs must use real services (no placeholders):
  - https://github-readme-streak-stats.herokuapp.com
  - https://github-profile-summary-cards.vercel.app
  - https://github-readme-activity-graph.vercel.app
- Theme: Tokyo Night / neon blue (`hide_border=true`, `bg_color=0d1117`)
- All elements centered with `<p align="center">`
- Output exactly **2 visual rows**, no more

## Styles
1. **Split Dashboard** — Streak + Summary Stats side by side (row 1) · Activity Graph full width (row 2)
2. **Hero Header** — Large Summary Card centered (row 1) · Streak + Activity Graph side by side (row 2)
3. **Minimal Dev** — Streak centered (row 1) · Activity Graph full width (row 2) *(no summary cards)*
4. **Cyber Neon** — Streak + Activity Graph layered and centered (row 1) · Summary Stats below (row 2)
5. **Data Dashboard** — Summary Stats (row 1) · Streak + Activity Graph side by side (row 2)

## Output
Single Markdown block, ready to paste into README.md.
    '''

    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
