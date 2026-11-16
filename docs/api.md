# API жоспары (6-сабақ)

Жол ережесі: `/api/` + кесте атауы көпше + керек болса `{id}`; жолда етістік жоқ,
тек ерекше әрекеттер (`/publish`, `/review`, `/attempts`, `/stats`).

| Әдіс   | Жол                            | Кім                      | Не істейді                                        | Story | Кесте                          |
|--------|--------------------------------|--------------------------|---------------------------------------------------|-------|--------------------------------|
| POST   | /api/quizzes                   | mentor                   | практикалық тест құру (жоспар)                    | US-4  | quizzes                        |
| POST   | /api/quizzes/{id}/questions    | mentor (иесі)            | сұрақ қосу (4 нұсқа, 1 дұрыс, тақырып)            | US-4  | questions                      |
| POST   | /api/quizzes/{id}/publish      | mentor (иесі)            | тестті жариялау (сұрағы 0 → 400)                  | US-4  | quizzes                        |
| GET    | /api/quizzes                   | student                  | жарияланған тесттер тізімі                        | US-1  | quizzes                        |
| GET    | /api/quizzes/{id}              | student (жарияланғанда)  | тест мәліметі + сұрақтар (correct_index-сіз)      | US-1  | quizzes, questions             |
| POST   | /api/quizzes/{id}/attempts     | student                  | жауаптарды жіберу; жауапта `score`                | US-1  | attempts, attempt_answers      |
| POST   | /api/attempts/{id}/review      | student (иесі)           | AI шолу: әр қатенің дұрыс шешімі бойынша түсіндірме | US-2  | attempts, attempt_answers      |
| GET    | /api/attempts/me               | student                  | менің бұрынғы attempt-терім                        | US-5  | attempts                       |
| GET    | /api/topics/me                 | student                  | әлсіз тақырыптар картасы (menің attempt-терімнен) | US-3  | attempts, attempt_answers, questions |
| POST   | /api/mentor/students           | mentor                   | өз тобыма студент қосу                            | US-4  | mentor_students                |
| GET    | /api/mentor/students           | mentor                   | менің топымдағы студенттер                        | US-4  | mentor_students                |
| GET    | /api/mentor/stats              | mentor                   | топтың жиі қателескен тақырыптары (top-N)         | US-4  | attempts, attempt_answers, questions |
| POST   | /api/attempts/{id}/feedback    | mentor                   | оқушы attempt-іне кері байланыс                    | US-6  | attempts                       |

Ережелер: студентке арналған схемада `correct_index` БОЛМАЙДЫ (AGENTS.md).
AI шолу (US-2) жаңа кесте құрмайды — әр сұраныста Ollama арқылы generatеді;
AI қолжетпесе → fallback (дұрыс жауап кілті + ескерту).

## Жауап кодтары

| Код | Қарапайым тілмен      | Бұл жобадағы мысал                                    |
|-----|-----------------------|--------------------------------------------------------|
| 200 | Бәрі дұрыс            | тесттер/attempt-тер тізімі қайтты                      |
| 201 | Құрылды               | тест/сұрақ/attempt құрылды                             |
| 204 | Өшірілді, қайтарыс жоқ | (MVP-де DELETE жоқ — резерв)                            |
| 400 | Ереже бұзылды         | сұрағы 0 тестті жариялау; жарияланбаған тестке тапсыру  |
| 401 | Сіз кірмегенсіз       | токен жоқ                                              |
| 403 | Кірдіңіз, рұқсат жоқ  | student тест құрады; student басқаның review-ін алады  |
| 404 | Табылмады             | мұндай тест/attempt жоқ (немесе ол сіздің емес)         |
| 422 | Дерек пішімі қате     | нұсқа саны 4 емес; correct_index 0–3 арасында емес; topic бос |
