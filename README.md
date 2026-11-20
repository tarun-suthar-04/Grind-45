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
| 2026-11-07 | Django blog setup, model, and admin | Setting up the `BlogPractice` project and `blog` app, creating the `Post` model with publication dates, and registering it in Django admin. | `BlogPractice/blog/models.py`, `BlogPractice/blog/admin.py`, `BlogPractice/config/settings.py` · `a2b1061` |
| 2026-11-07 | Django blog URLs, views, and templates | Connecting the project URL configuration to a `blog` app, mapping the app's root URL to a view, and rendering a namespaced template with sample blog posts. | `BlogPractice/config/urls.py`, `BlogPractice/blog/urls.py`, `BlogPractice/blog/views.py`, `BlogPractice/blog/templates/blog/post_list.html` · `3861fe9` |
| 2026-11-09 | Django ORM querying and post detail view | Querying published posts from the database using timezone filters and adding a post detail view with `get_object_or_404` and dynamic URL routing. | `BlogPractice/blog/views.py`, `BlogPractice/blog/urls.py`, `BlogPractice/blog/templates/blog/post_detail.html`, `BlogPractice/blog/templates/blog/post_list.html` · `deef73c` |
| 2026-11-09 | Django ModelForm and post creation | Creating `PostForm` using `forms.ModelForm`, handling form submission and validation in `post_new` view, and redirecting to the detail view. | `BlogPractice/blog/forms.py`, `BlogPractice/blog/views.py`, `BlogPractice/blog/urls.py`, `BlogPractice/blog/templates/blog/post_edit.html` · `c1bff21` |
| 2026-11-17 | Django post edit view | Reusing `PostForm` with an instance to edit existing posts via `post_edit` view, and adding an edit button to the detail page. | `BlogPractice/blog/views.py`, `BlogPractice/blog/urls.py`, `BlogPractice/blog/templates/blog/post_detail.html` · `d2d214b` |
| 2026-11-17 | Static files and CSS styling | Adding a custom stylesheet for headers, post layouts, and action buttons, loaded via `{% load static %}` in templates. | `BlogPractice/blog/static/css/blog.css`, `BlogPractice/blog/templates/blog/post_list.html`, `BlogPractice/blog/templates/blog/post_detail.html` · `be3d534` |

## Where to look

| Folder | Learning area |
|---|---|
| `python/` | Python exercises, text files, and JSON examples. |
| `SQL/` | Database schema, sample data, and query practice. |
| `DSA/` | Reserved for data structures and algorithms exercises. |
| `DjangoLearning/` | Django project with `core` and `orders` apps. |
| `BlogPractice/` | Django blog project with a `blog` app, models, admin, ModelForm, CRUD views, templates, and static CSS styling. |

## DjangoLearning routes

- `/admin/` — Django administration.
- `/orders/` — renders `index.html` with developer and mentor data supplied by the view.
- `/` — also maps to the orders view.
- `core/urls.py` defines a `hello/` route, but the core URL configuration is not currently included in the project routes.

## BlogPractice routes

- `/` — routes to the blog app's `post_list` view, which queries published posts from the database and renders `blog/post_list.html`.
- `/post/<int:pk>/` — routes to `post_detail` view, retrieving a single post by primary key (`get_object_or_404`) and rendering `blog/post_detail.html`.
- `/post/new/` — routes to `post_new` view, displaying and processing `PostForm` to create and publish a new post.
- `/post/<int:pk>/edit/` — routes to `post_edit` view, pre-populating `PostForm` with an existing post to allow editing and updating.


[![Architecture diagram of tarun-suthar-04/grind-45](https://gitdiagram.com/tarun-suthar-04/grind-45/diagram.png)](https://gitdiagram.com/tarun-suthar-04/grind-45?utm_source=readme&utm_medium=picture)

## Continue the log

When new work is committed, add a row with its date, the specific concept practiced, the relevant file, and commit ID. Keep the explanation focused on what the code currently shows; leave dates and topics blank until they are actually completed.
