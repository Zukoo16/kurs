from datetime import date

from hello import format_greeting


def test_format_greeting_with_custom_name() -> None:
    test_date = date(2026, 11, 6)
    assert format_greeting("Әли", today=test_date) == "Сәлем, Әли! Бүгін 06.11.2026"


def test_format_greeting_with_default_fallback() -> None:
    test_date = date(2026, 11, 6)
    assert format_greeting("", today=test_date) == "Сәлем, Досым! Бүгін 06.11.2026"
    assert format_greeting("   ", today=test_date) == "Сәлем, Досым! Бүгін 06.11.2026"
    assert format_greeting(None, today=test_date) == "Сәлем, Досым! Бүгін 06.11.2026"


def test_format_greeting_default_date() -> None:
    result = format_greeting("Айгүл")
    today_str = date.today().strftime("%d.%m.%Y")
    assert result == f"Сәлем, Айгүл! Бүгін {today_str}"

