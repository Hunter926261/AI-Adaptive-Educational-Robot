import re

# Common synonym mapping
SYNONYMS = {
    "ai": ["artificial intelligence", "machine intelligence"],
    "learn": ["study", "understand", "know"],
    "teach": ["explain", "train", "guide"]
}


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    for base, variants in SYNONYMS.items():
        for v in variants:
            text = text.replace(v, base)

    return text
