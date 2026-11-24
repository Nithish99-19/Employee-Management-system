# Employee Management System

A dynamic web-based Employee Management System built with **Python / Django**, a **SQL database** (SQLite by default, PostgreSQL optional) and a **Bootstrap + JavaScript GUI**.

## Features
**Dynamic interface (no page reloads)**
- **Register / edit employees in a pop-up form** with instant validation errors; **delete with a confirmation dialog**
- **Live search** as you type, plus department, status and page-size filters; **click column titles to sort**
- **Bulk actions**: tick several rows, then set their status or delete them in one go
- **Search suggestions** in the top bar (type 2+ letters), with keyboard shortcuts: `/` to search, `n` to register an employee
- **Change status in place** from a dropdown in any table
- **Live dashboard**: animated counters and four charts (headcount, status, average salary per department, hires per year) that refresh every 15 seconds and immediately after any change
- **Full dataset table on the dashboard** with instant filter, sortable columns and Edit / Delete buttons
- **Dark mode** toggle (remembered in the browser)
- **CSV export** (respects filters) and **CSV import** (a 60-employee sample dataset loads on first run)

**Back end**
- Login-protected access (Django authentication) and Django admin
- Departments (deletion blocked while a department has employees)
- SQLite by default, PostgreSQL optional
- Automated tests for models, views, JSON/HTML-fragment endpoints, importer

## Run it in VS Code (easiest)
1. Install Python 3.10+ and VS Code with the **Python** extension.
2. **File > Open Folder** and choose this project.
3. Open the terminal (Ctrl + `) and run:
   ```bash
   python bootstrap.py
   ```
   This creates `.venv`, installs Django, creates the database, adds demo data and a demo admin login, starts the server and opens your browser.
4. Log in with **admin / admin123** (demo only, change it for real use).

Next time: press **F5** and choose **EMS: run app (setup + server)**. Press **Ctrl+Shift+P > Python: Select Interpreter** and pick the `.venv` one if VS Code has not already.

The app opens at `http://127.0.0.1:8000/`.

Other launch configurations: **EMS: runserver only** and **EMS: run tests**. Tasks are under **Terminal > Run Task**.

## Manual setup (any terminal)
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations employees
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo       # optional
python manage.py runserver
```

## Load your own dataset
Use the **Import CSV** button on the Employees page, or from the terminal:
```bash
python manage.py import_employees path/to/your_file.csv
```
Columns: `First name, Last name, Email, Phone, Department, Job title, Salary, Hire date, Status`
(Phone and Status optional; dates as `YYYY-MM-DD`; status Active / On leave / Terminated).
Existing emails are updated, new ones are added, and bad rows are skipped with a message.
The file from **Export CSV** can be re-imported unchanged.

## Run tests
```bash
python manage.py test
```

## Use PostgreSQL instead of SQLite
```bash
pip install psycopg2-binary
export DB_ENGINE=postgres DB_NAME=ems DB_USER=postgres DB_PASSWORD=secret DB_HOST=localhost
python manage.py migrate
```

## Project layout
```
bootstrap.py   one-command setup (venv + install + run)
run.py         migrate, seed, start server, open browser
.vscode/       launch, tasks and settings for VS Code
ems_project/   settings, root URLs, WSGI
employees/     models, forms, views, urls, admin, tests, CSV importer, seed command
data/          employees_sample.csv (60 sample employees)
templates/     base layout, login, dashboard, employee and department pages
docs/          technical documentation (DESIGN.md)
```

See [docs/DESIGN.md](docs/DESIGN.md) for requirements, design and testing details.
