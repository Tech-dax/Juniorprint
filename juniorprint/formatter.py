import re
from .styles import COLORS, STYLES, RESET

pattern = re.compile(r'([a-z]+)_\[(.*?)\]')

def format_text(text: str) -> str:
    def repl(match):
        key, content = match.group(1), match.group(2)
        codes = ""
        for char in key:
            if char in COLORS:
                codes += COLORS[char]
            elif char in STYLES:
                codes += STYLES[char]
        return f"{codes}{content}{RESET}"
    return pattern.sub(repl, text)
