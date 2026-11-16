# API жоспары (6-сабақ)

Жол ережесі: `/api/` + кесте атауы көпше + керек болса `{id}`; жолда етістік жоқ,
тек ерекше әрекеттер (`/publish`, `/attempts`, `/generate-questions`).

| Әдіс   | Жол                            | Кім                      | Не істейді                          | Story  | Кесте                 |
|--------|--------------------------------|--------------------------|-------------------------------------|--------|-----------------------|
| POST   | /api/quizzes                   | teacher                  | тест құру (жоспарлау)               | US-1   | quizzes               |
| GET    | /api/quizzes/me                | teacher (иесі)           | өз тесттерінің тізімі               | US-1   | quizzes               |
| GET    | /api/quizzes/{id}              | teacher (иесі); student — жарияланғанда | тест мәліметі + сұрақтар (нұсқалармен, дұрыс индекссіз) | US-1, US-3 | quizzes, questions |
| PATCH  | /api/quizzes/{id}              | teacher (иесі)           | жоспардағы тестті түзету            | US-1   | quizzes               |
| DELETE | /api/quizzes/{id}              | teacher (иесі)           | тестті өшіру (тапсырылуы болмаса)   | US-1   | quizzes               |
| POST   | /api/quizzes/{id}/questions    | teacher (иесі)           | сұрақ қосу (2–6 нұсқа, 1 дұрыс)     | US-1   | questions             |
| POST   | /api/quizzes/{id}/publish      | teacher (иесі)           | тестті жариялау (сұрағы 0 → 400)   | US-2   | quizzes               |
| GET    | /api/quizzes                   | student (жарияланғандар) | жарияланған тесттер тізімі          | US-3   | quizzes               |
| POST   | /api/quizzes/{id}/attempts     | student                  | жауаптарды жіберу; жауапта `score`  | US-3   | attempts              |
| GET    | /api/attempts/me               | student                  | менің бұрынғы нәтижелерім            | US-5   | attempts              |
| POST   | /api/ai/generate-questions     | teacher                  | мәтіннен сұрақ ұсынысы (JSON)       | US-4   | — (сақтау US-1 арқылы)|

Ереже: AI ұсынысын тікелей DB-ге жазатын endpoint жоқ — мұғалім `POST …/questions`
арқылы өзі қосады (US-4 шарты).

## Жауап кодтары

| Код | Қарапайым тілмен      | Бұл жобадағы мысал                          |
|-----|-----------------------|---------------------------------------------|
| 200 | Бәрі дұрыс            | тесттер тізімі қайтты                       |
| 201 | Құрылды               | жаңа тест/сұрақ/attempt құрылды             |
| 204 | Өшірілді, қайтарыс жоқ | тест өшірілді                               |
| 400 | Ереже бұзылды         | сұрағы 0 тестті жариялау; тапсырылмаған тестке attempt |
| 401 | Сіз кірмегенсіз       | токен жоқ                                   |
| 403 | Кірдіңіз, рұқсат жоқ  | student /api/quizzes-ке POST; басқаның attempt-ін оқу |
| 404 | Табылмады             | мұндай тест/сұрақ жоқ                       |
| 422 | Дерек пішімі қате     | атауы 2 таңба; нұсқаның саны 1 немесе 7; correct_index шетінен тыс |

## Сәйкестік: story → endpoint → кесте

| Story | Endpoint | Кесте |
|---|---|---|
| US-1 (M) тест құру, сұрақ қосу | POST /api/quizzes · POST /api/quizzes/{id}/questions · GET /api/quizzes/me · GET /api/quizzes/{id} · PATCH /api/quizzes/{id} · DELETE /api/quizzes/{id} | quizzes, questions |
| US-2 (M) жариялау | POST /api/quizzes/{id}/publish | quizzes |
| US-3 (M) тапсыру, ұпай | GET /api/quizzes · GET /api/quizzes/{id} · POST /api/quizzes/{id}/attempts | quizzes, questions, attempts |
| US-4 (M) AI ұсынысы | POST /api/ai/generate-questions | — (сақтау US-1 арқылы: questions) |
| US-5 (S) өз нәтижелерім | GET /api/attempts/me | attempts |
