# NutriTrack — Django Progress Tracking & Blogs

A beginner-friendly Django web app matching the requested **Progress Tracking & Blogs** idea.

## Features

- Dashboard with summary cards
- Weight progress chart
- Daily calorie chart
- Progress CRUD: Create, Read, Update, Delete
- Search progress notes
- Blog CRUD
- Blog search
- Django admin panel
- SQLite database
- Responsive UI

## Run on Windows

Open the project folder in VS Code terminal:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open:

`http://127.0.0.1:8000/`

Admin:

```bash
python manage.py createsuperuser
```

Then visit:

`http://127.0.0.1:8000/admin/`

## Project structure

```text
nutrition_tracker_django/
│
├── manage.py
├── requirements.txt
├── db.sqlite3              # created after migrate
├── nutrition/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── progress_tracking/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── progress/
│   └── blogs/
│
└── static/
    └── css/style.css
```
