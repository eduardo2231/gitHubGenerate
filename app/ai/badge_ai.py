# from google import genai
from groq import Groq
import streamlit as st
import re

def generate_badges(tech: str, api: str, style_badge) -> str:

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
    {tech}' and which following style {style_badge}, if dont exists, use the standard style flat'''
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

def generate_stats(user: str, api: str, style_stats) -> str:
    prompt = f'''Create a GitHub README section using ONLY Markdown (GitHub Flavored Markdown).
    
    GitHub username: {user} and style that was choice: {style_stats}
    
    STRICT RULES:
- Output ONLY Markdown (no explanations, no comments)
- Everything must be directly renderable on GitHub
- DO NOT use placeholders like STREAK_STATS_URL
- All image URLs must be real working links from GitHub stats services
- Use only these services:
  - https://github-readme-streak-stats.herokuapp.com
  - https://github-profile-summary-cards.vercel.app
  - https://github-readme-activity-graph.vercel.app
- Use dark theme style (Tokyo Night / neon blue / cyber aesthetic)
- Background color: #0d1117
- No borders (hide_border=true)
- Everything centered using <p align="center">

REQUIRED COMPONENTS:
1. GitHub Streak Stats
2. GitHub Profile Summary Cards (stats)
3. GitHub Activity Graph

LAYOUT RULES:
- First row: Streak + Summary Stats (side by side, centered)
- Second row: Activity Graph full width
- Clean spacing between sections
- Professional developer profile layout
    
    1. SPLIT DASHBOARD STYLE
    - Streak + Stats side-by-side (centered row)
    - Activity graph below full width
    - Balanced dashboard look
    
    2. HERO HEADER STYLE
    - Large centered stats first (summary card)
    - Streak below
    - Activity graph at bottom
    - Feels like a profile landing page
    
    3. MINIMAL DEVELOPER STYLE
    - Only Streak + Activity Graph
    - No summary cards
    - Very clean and lightweight
    
    4. CYBER NEON STYLE
    - All elements centered in layers
    - Strong neon blue/cyan theme
    - Slight visual emphasis on activity graph
    - Dense but aesthetic layout
    
    5. DATA DASHBOARD STYLE
    - Stats first (summary cards)
    - Streak next
    - Activity graph last
    - Structured like an analytics dashboard
    
    OUTPUT:
    - One single Markdown block ready to paste into README.md
    - Must be immediately visualizable on GitHub
    '''

    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content