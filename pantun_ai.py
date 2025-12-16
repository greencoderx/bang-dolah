from openai import OpenAI
import random

client = OpenAI()

def generate_pantun():
    themes = [
        "kehidupan",
        "nasihat",
        "iman",
        "ilmu",
        "kesabaran",
        "syukur"
    ]

    theme = random.choice(themes)

    prompt = f"""
Cipta satu pantun Melayu 4 baris bertema {theme}.
Syarat:
- Bahasa Melayu
- Berima (ABAB atau AABB)
- Unsur nasihat atau kebaikan
- Sesuai untuk Twitter (maks 280 aksara)
- Jangan guna emoji berlebihan (maks 1)
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    pantun = response.choices[0].message.content.strip()
    return pantun
