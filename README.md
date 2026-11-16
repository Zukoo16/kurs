# AIDD Platform

AI-Driven Development курсының негізгі жобасы.

Платформа заманауи микросервистік архитектураға, жергілікті ЖИ (LLM — Ollama) мүмкіндіктеріне және Keycloak OIDC рөлдік қауіпсіздік моделіне негізделген.

---

## Тақырып

ҰБТ/кешенді тестілеуге дайындалатын 18+ студенттер пробный тест тапсырып, қателерін қолмен талдайды — ұзақ және жүйесіз; платформа әр қатені түсінуді және әлсіз тақырыптарды көруді жеңілдетеді.

**Мақсатты пайдаланушылар:** ҰБТ және кешенді тестілеуге дайындалатын 18+ студенттер және оларды дайындайтын куратор-менторлар.

**Сұхбатқа:** 5 адам: 3 студент (18–19 жас, ҰБТ тапсырған) + 2 куратор-ментор (21–22 жас, дайындық орталығы) — жоспар `docs/fieldwork/guide.md`-де.

**Рөлдер жүйеде:** student (дайындалушы), mentor (куратор).

**AI идеясы:** Ollama (жергілікті LLM) пробный тесттегі әр қателі сұрақтың дұрыс шешімін түсіндіреді және әлсіз тақырыптар картасын жасайды; ментор — топтың жалпы қателер тізімін алады.

**Бекітілді:** бекіту күтуде (оқытушы)

---

## 🛠 Технологиялық стек

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.12+)
* **Деректер қоры & ORM:** PostgreSQL 16 + [SQLAlchemy 2.0](https://www.sqlalchemy.org/) + Alembic
* **Аутентификация & Авторизация:** [Keycloak](https://www.keycloak.org/) (OIDC, рөлдер: `student`, `teacher`, `admin`)
* **Жергілікті LLM:** [Ollama](https://ollama.com/) (`llama3.2` моделі)
* **Кэштеу:** Redis 7
* **Асинхронды кезек & Worker:** RabbitMQ 3 + фондық өңдеуші (Worker)
* **Frontend:** Next.js 16 (`web/`)
* **Кері прокси (Reverse Proxy):** Nginx
* **Оркестрация:** Docker Compose
* **Тестілеу:** pytest (9.x)

---

## 📂 Жоба құрылымы

```text
├── backend/                       # FastAPI қосымшасы
│   ├── app/
│   │   ├── api/v1/                # REST API эндпоинттары (health, auth, llm)
│   │   ├── core/                  # Конфигурация мен Keycloak OIDC күзеті
│   │   ├── db/                    # SQLAlchemy 2 сессиясы мен базалық класс
│   │   ├── models/                # Деректер моделі (UserProfile)
│   │   ├── schemas/               # Pydantic схемалары
│   │   └── llm/                   # Ollama интеграциялық клиенті
│   ├── tests/                     # Бэкенд pytest тесттері
│   ├── Dockerfile
│   └── requirements.txt
├── web/                           # Next.js 16 қолданбасы
│   ├── src/app/                   # App Router беттері
│   ├── package.json
│   └── Dockerfile
├── worker/                        # RabbitMQ асинхронды өңдеушісі
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx/                         # Nginx конфигурациясы
│   └── nginx.conf
├── tests/                         # Негізгі модульдік тесттер
├── docker-compose.yml             # Барлық сервистердің конфигурациясы
├── .env.example                   # Баптаулар шаблоны
└── AGENTS.md                      # Жобаның AI агент ережелері
```

---

## 🚀 Іске қосу (Docker Compose)

1. **Конфигурациялық `.env` файлын дайындау:**
   ```bash
   cp .env.example .env
   ```

2. **Барлық сервистерді контейнерде көтеру:**
   ```bash
   docker compose up -d --build
   ```

3. **Қолжетімді сервистер:**
   * **Nginx Entrypoint:** [http://localhost](http://localhost)
   * **FastAPI Docs (Swagger UI):** [http://localhost:8000/docs](http://localhost:8000/docs)
   * **Keycloak Console:** [http://localhost:8080](http://localhost:8080)
   * **RabbitMQ Management:** [http://localhost:15672](http://localhost:15672) (guest/guest)
   * **Ollama API:** [http://localhost:11434](http://localhost:11434)
   * **Next.js Web:** [http://localhost:3000](http://localhost:3000)

---

## 🧪 Тесттерді іске қосу

```bash
# Виртуалды ортаны іске қосу
source .venv/bin/activate

# Тесттерді орындау
pytest -v
```
