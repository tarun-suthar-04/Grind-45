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
| 2026-11-01 | Django templates and view context | Passing a developer name and a list from a view to an HTML template, then rendering the list with a template loop. | `DjangoLearning/orders/views.py`, `DjangoLearning/templates/index.html` · `0380b8c` |
| 2026-11-07 | Django blog URLs, views, and templates | Connecting the project URL configuration to a `blog` app, mapping the app's root URL to a view, and rendering a namespaced template with sample blog posts. | `BlogPractice/config/urls.py`, `BlogPractice/blog/urls.py`, `BlogPractice/blog/views.py`, `BlogPractice/blog/templates/blog/post_list.html` · `3861fe9` |

## Where to look

| Folder | Learning area |
|---|---|
| `python/` | Python exercises, text files, and JSON examples. |
| `SQL/` | Database schema, sample data, and query practice. |
| `DSA/` | Reserved for data structures and algorithms exercises. |
| `DjangoLearning/` | Django project with `core` and `orders` apps. |
| `BlogPractice/` | Django blog project with a `blog` app, URL routing, view, and post list template. |

## DjangoLearning routes

- `/admin/` — Django administration.
- `/orders/` — renders `index.html` with developer and mentor data supplied by the view.
- `/` — also maps to the orders view.
- `core/urls.py` defines a `hello/` route, but the core URL configuration is not currently included in the project routes.

## BlogPractice route

- `/` — routes to the blog app's `post_list` view, which renders `blog/post_list.html`.

[![Architecture diagram of tarun-suthar-04/grind-45](https://gitdiagram.com/tarun-suthar-04/grind-45/diagram.png)](https://gitdiagram.com/tarun-suthar-04/grind-45?utm_source=readme&utm_medium=picture)

## Continue the log

When new work is committed, add a row with its date, the specific concept practiced, the relevant file, and commit ID. Keep the explanation focused on what the code currently shows; leave dates and topics blank until they are actually completed.
