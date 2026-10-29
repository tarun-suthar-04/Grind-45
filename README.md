# Grind-45: 45 Days of Python and Development

A hands-on learning repository for building programming fundamentals through short, practical exercises. Work is organized by topic and grows as new tools and projects are learned. The Django project is part of that learning journey.

## Learning process

Use each study session to learn one focused concept, practice it in code, and record what you learned:

1. **Choose a small topic** from Python, SQL, data structures and algorithms, or Django.
2. **Study the concept** using notes or a tutorial, then write a short summary in your own words.
3. **Practice** with a small exercise or a feature in the Django project.
4. **Run and review** the code; fix errors and note what caused them.
5. **Save the work** in the matching folder and make a Git commit with a clear message.
6. **Update the progress log** below with the date, topic, outcome, and next step.

Keep tasks small enough to finish in a session. Prefer understanding and explaining the code over copying a solution. Revisit unfinished topics in a later session rather than marking them complete prematurely.

## Repository map

| Path | Purpose |
|---|---|
| `python/` | Python practice programs and sample data for file handling, collections, JSON, and debugging. |
| `SQL/` | SQL schema, seed data, and query exercises. |
| `DSA/` | Data structures and algorithms practice. |
| `DjangoLearning/` | Django learning project, including the `core` and `orders` apps. |

## Django project quick start

The Django project lives in `DjangoLearning/`. On Windows PowerShell, from the repository root:

```powershell
cd DjangoLearning
.\.venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/orders/` to see the current orders view, or `http://127.0.0.1:8000/admin/` for the Django admin. The project root (`/`) currently has no route, so it returns a 404. The `core` app has a `hello/` view, but its URL configuration is not currently included by the project URL configuration.

If the virtual environment does not exist, create one and install Django 5.2:

```powershell
cd DjangoLearning
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install "Django>=5.2,<5.3"
python manage.py migrate
python manage.py runserver
```

After changing a model, create and apply migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

## Progress log

Record actual study sessions as they happen; dates and topics below are examples of the intended format, not a fixed schedule.

| Session | Date | Focus | Practice / outcome | Next step |
|---|---|---|---|---|
| Setup |  | Git and repository setup | Repository created | Continue with a focused topic |
| 1 |  | Python, SQL, or DSA fundamentals |  |  |
| 2 |  | Django project structure and URL routing | `core` and `orders` apps created; `/orders/` is routed | Connect or extend a view |

## Git and local files

Commit source code and learning notes. Keep machine-specific or generated files local: `DjangoLearning/.venv/`, `DjangoLearning/db.sqlite3`, and Python `__pycache__/` directories are ignored. Keep passwords and secret keys out of commits; use environment variables for secrets before sharing or deploying the project.
