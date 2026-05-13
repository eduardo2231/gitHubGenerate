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

        GitHub username: {user} and style chosen: {style_stats}

        STRICT RULES:
    - Output ONLY Markdown (no explanations, no comments, no code blocks)
    - Everything must be directly renderable on GitHub
    - DO NOT use placeholders like STREAK_STATS_URL
    - All image URLs must be real working links from GitHub stats services
    - Use only these services:
      - https://github-readme-streak-stats.herokuapp.com
      - https://github-profile-summary-cards.vercel.app
      - https://github-readme-activity-graph.vercel.app
    - Background color: #0d1117
    - No borders (hide_border=true)
    - Everything centered using <p align="center">

    COMPONENTS:
    - Use only the components defined by the chosen style
    - Do not add components that are not part of the style layout

    AVAILABLE STYLES (use ONLY the one matching {style_stats}):
    1. Split Dashboard - Streak + Stats side by side, activity graph full width below
    2. Hero Header - Large centered summary card first, streak below, activity graph at bottom
    3. Minimal Developer - Only streak + activity graph, no summary cards, clean and lightweight
    4. Cyber Neon - All elements centered in layers, strong neon blue/cyan theme, activity graph emphasis
    5. Data Dashboard - Stats first, streak next, activity graph last, analytics layout
    6. Terminal Dark - Monospace feel, dark green accent, minimal spacing
    7. Glassmorphism - Soft transparent feel, light borders, pastel accents
    8. Hacker Grid - Dense grid layout, all stats packed together, matrix aesthetic
    9. Sunset Gradient - Warm orange/pink theme, streak centered as hero
    10. Arctic Ice - Cold blue/white palette, clean lines, minimalist nordic style
    11. Retro Wave - Purple/pink neon, synthwave aesthetic, layered layout
    12. Forest Green - Earth tones, green accents, calm and clean layout
    13. Midnight Purple - Deep purple theme, streak as centerpiece, cards below
    14. Monochrome - Pure black and white, no color accents, typography-focused
    15. Neon Orange - Bright orange highlights, dark background, bold layout
    16. Deep Space - Cosmic dark theme, blue/indigo accents, cards in orbit layout
    17. Red Matrix - Red neon on black, hacker aesthetic, compact layout
    18. Gold Elite - Gold/yellow accents, premium feel, dashboard layout
    19. Pastel Soft - Soft pink/purple/blue pastel palette, friendly and light
    20. Classic Blue - Traditional GitHub blue theme, professional and clean

    OUTPUT RULES:
    - Return ONLY ONE style: the one matching {style_stats}
    - One single Markdown block ready to paste into README.md
    - Must be immediately visualizable on GitHub
    - No extra text, no explanations, no alternatives
        '''

    client = Groq(api_key=api)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content