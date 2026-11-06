#!/usr/bin/env python3
"""Сәлемдесу скрипті: «Сәлем, <аты>! Бүгін <күн.ай.жыл>» деп шығарады.

Пайдалану:
    python hello.py             # атты қолмен сұрайды
    python hello.py --name Әли  # ат аргументпен беріледі

Тек стандартты кітапхана.
"""

import argparse
from datetime import date


def main() -> None:
    parser = argparse.ArgumentParser(description="Сәлемдесу скрипті")
    parser.add_argument("--name", help="атыңыз (берілмесе сұралады)")
    args = parser.parse_args()

    name = args.name or input("Атыңыз: ").strip() or "Досым"
    today = date.today().strftime("%d.%m.%Y")
    print(f"Сәлем, {name}! Бүгін {today}")


if __name__ == "__main__":
    main()
