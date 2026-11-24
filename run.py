"""Prepare the database and start the dev server. Works with F5 / Run in VS Code.

Usage:  python run.py            (Django must be installed; use bootstrap.py otherwise)
"""
import os
import sys
import threading
import webbrowser

HOST, PORT = "127.0.0.1", 8000


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ems_project.settings")
    import django
    from django.core.management import call_command

    django.setup()

    # The auto-reloader re-runs this file in a child process; do setup only once.
    if os.environ.get("RUN_MAIN") != "true":
        call_command("makemigrations", "employees", interactive=False, verbosity=0)
        call_command("migrate", interactive=False, verbosity=0)

        from django.contrib.auth import get_user_model
        from employees.models import Employee

        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            print("\nCreated demo login ->  username: admin   password: admin123")
            print("(change it before using this anywhere real)\n")
        if not Employee.objects.exists():
            sample = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "employees_sample.csv")
            if os.path.exists(sample):
                call_command("import_employees", sample)
            else:
                call_command("seed_demo")

        threading.Timer(1.5, lambda: webbrowser.open(f"http://{HOST}:{PORT}/")).start()

    call_command("runserver", f"{HOST}:{PORT}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
