# Grind-45: Learning Log

A date-wise record of the Python, SQL, and Django topics practiced in this repository. Each entry links the topic to the code or SQL files that demonstrate it. Commit IDs show the related work in Git history.

## Topics by date

| Date | Topic | What the code demonstrates | Files / commits |
|---|---|---|---|
| 2026-10-20 | SQL tables and sample data | Creating a small order-management schema with customers, products, orders, and order items; inserting records. | `SQL/schema.sql`, `SQL/seed.sql` · `53e67e4` |
| 2026-10-20 | SQL `SELECT` | Reading rows from a table with a basic query. | `SQL/queries.sql` · `4491464` |
| 2026-10-20 | Python file reading | Exploring `read()`, `readline()`, and `readlines()` with a text file. | `python/sample.txt` · `06ee5cd` |
| 2026-10-29 | File input and output | Collecting names from input and writing/reading text files; trying file modes and measuring file content. | `python/practice.py`, `python/main.py` · `d9c9064`, `47f890e` |
| 2026-10-29 | Reading and processing text files | Using list comprehensions to filter values; counting words; searching lines and summing valid integers while handling file errors. | `python/listcomprehension.py`, `python/count_words.py` · `a76e5af`, `ddfc312` |
| 2026-10-29 | JSON | Loading and saving JSON data, reading a list of cities, adding an entry, and handling missing or invalid data. | `python/jsonpractice.py`, `python/cities.json`, `python/sample.json`, `python/dumpdata.json` · `31a4187`, `2b228be` |
| 2026-10-29 | Debugging | Pausing execution with Python's `pdb` debugger. | `python/debugging.py` · `9549070` |
| 2026-10-29 | Django project and URL routing | Setting up a Django project and `orders` app, returning a response from a view, and routing `/orders/` to it. | `DjangoLearning/manage.py`, `DjangoLearning/orders/`, `DjangoLearning/MydjangoProject/urls.py` · `88fa20a` |

## Where to look

| Folder | Learning area |
|---|---|
| `python/` | Python exercises, text files, and JSON examples. |
| `SQL/` | Database schema, sample data, and query practice. |
| `DSA/` | Reserved for data structures and algorithms exercises. |
| `DjangoLearning/` | Django project with `core` and `orders` apps. |

## Current Django routes

- `/admin/` — Django administration.
- `/orders/` — the orders app's current response view.
- `/` — not configured yet, so it returns a 404.
- `core/urls.py` defines a `hello/` route, but the core URL configuration is not currently included in the project routes.

## Continue the log

When new work is committed, add a row with its date, the specific concept practiced, the relevant file, and commit ID. Keep the explanation focused on what the code currently shows; leave dates and topics blank until they are actually completed.
