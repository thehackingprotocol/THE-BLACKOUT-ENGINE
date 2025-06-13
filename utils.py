import re

def safe_int_input(prompt, default=10):
    try:
        val = input(prompt).strip()
        return int(val) if val else default
    except:
        return default

def normalize_target(url):
    return f"https://{url}" if not re.match(r"^https?://", url) else url
