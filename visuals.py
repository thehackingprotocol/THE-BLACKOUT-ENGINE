from pyfiglet import Figlet
from termcolor import cprint, colored
import random

fonts = [
    "slant", "block", "big", "banner3-D", "colossal", "larry3d", "speed"
]
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def banner():
    f = Figlet(font=random.choice(fonts))
    title = f.renderText("THE BLACKOUT ENGINE")
    subtitle = "🧠 POWERED BY KHORA // EXECUTED BY THE HACKING PROTOCOL"
    tagline1 = "⚡ MAX SATURATION  •  ☁ WAF BYPASS  •  🧬 TLS OBFUSCATION"
    tagline2 = "👻 ANONYMIZED LAUNCH  •  🔥 MILITARY GRADE  •  🕶 GEN-Z OPS SUITE"

    bar = "=" * 80
    cprint(bar, random.choice(colors), attrs=["bold"])
    cprint(title, random.choice(colors), attrs=["bold"])
    cprint(subtitle.center(80), random.choice(colors), attrs=["bold"])
    cprint(tagline1.center(80), random.choice(colors))
    cprint(tagline2.center(80), random.choice(colors))
    cprint(bar, random.choice(colors), attrs=["bold"])
    print()

def dynamic_input(prompt):
    color = random.choice(colors)
    style = random.choice(["bold", "underline", "reverse"])
    return input(colored(prompt + " ", color, attrs=[style]))
