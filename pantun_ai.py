from openai import OpenAI
import random
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

USED_RHYMES_FILE = "data/used_rhymes.txt"

def load_used_rhymes():
    try:
        with open(USED_RHYMES_FILE, "r", encoding="utf-8") as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def save_rhyme(rhyme):
    with open(USED_RHYMES_FILE, "a", encoding="utf-8") as f:
        f.write(rhyme + "\n")

def extract_rhyme(pantun):
    lines = [l for l in pantun.split("\n") if l.strip()]
    endings = []
    for line in lines:
        word = line.strip().split()[-1]
        endings.append(word[-3:].lower())
    return "-".join(endings)

def generate_pantun():
    themes = [
        "adat Aceh",
        "nasihat kehidupan",
        "iman dan akhlak",
        "ilmu dan kesabaran",
        "syukur dan tawakal"
    ]

    theme = random.choice(themes)
    used_rhymes = load_used_rhymes()

    prompt = f"""
Cipta satu pantun Melayu gaya Aceh, 4 baris.
Tema: {theme}

Ciri wajib:
- Unsur kearifan lokal Aceh
- Nada tenang dan beradab
- Nilai iman, adat, atau akhlak
- Bahasa Melayu baku
- Skema rima jelas (ABAB atau AABB)
- Maksimum 1 emoji
- Sesuai untuk Twitter (≤280 aksara)
"""

    for _ in range(3):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )

        pantun = response.choices[0].message.content.strip()
        rhyme = extract_rhyme(pantun)

        if rhyme not in used_rhymes:
            save_rhyme(rhyme)
            return pantun

    return pantun

def translate_to_english(pantun):
    prompt = f"""
Translate the following pantun into natural English.
Preserve poetic meaning, not literal wording.

Pantun:
{pantun}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()
