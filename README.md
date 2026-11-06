# aidd-zukoo16

AI-Driven Development курсы — жеке жоба репозиторийі (1-апта).

## Мақсаты

Бірінші Python-прожектің даму ортасы (venv, Git, GitHub) мен «тармақ → коммит → PR → merge» жұмыс тәртібін меңгеру.

## Не істейді

`hello.py` — сәлемдесу скрипті: атыңызды сұрап (немесе `--name` аргументімен ала) «Сәлем, <аты>! Бүгін <күн.ай.жыл>» деп шығарады. Тек стандартты кітапхана.

## Іске қосу

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python hello.py                  # атты қолмен енгізу
python hello.py --name Әли       # ат аргументпен
```

## Тест

```bash
.venv/bin/pytest --version       # pytest ортада орнатылған (9.x)
```
