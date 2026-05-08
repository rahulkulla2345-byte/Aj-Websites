import re


def clean_text(text):

    text = re.sub(r'\\s+', ' ', text)

    junk_phrases = [
        "Accept cookies",
        "Cookie policy",
        "Privacy policy",
        "Terms of service",
    ]

    for phrase in junk_phrases:
        text = text.replace(phrase, "")

    return text.strip()
