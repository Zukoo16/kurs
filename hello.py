#!/usr/bin/env python3
"""Сәлемдесу скрипті: «Сәлем, <аты>! Бүгін <күн.ай.жыл>» деп шығарады.

Пайдалану:
    python hello.py             # атты қолмен сұрайды
    python hello.py --name Әли  # ат аргументпен беріледі

Тек стандартты кітапхана.
"""

import argparse
from datetime import date


def format_greeting(name: str | None = None, today: date | None = None) -> str:
    """Сәлемдесу мәтінін қалыптастырады."""
    user_name = (name or "").strip() or "Досым"
    current_date = (today or date.today()).strftime("%d.%m.%Y")
    return f"Сәлем, {user_name}! Бүгін {current_date}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Сәлемдесу скрипті")
    parser.add_argument("--name", help="атыңыз (берілмесе сұралады)")
    args = parser.parse_args()

    name = args.name
    if not name:
        try:
            name = input("Атыңыз: ")
        except (EOFError, KeyboardInterrupt):
            name = ""

    print(format_greeting(name))


if __name__ == "__main__":
    main()
