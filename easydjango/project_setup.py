import os
import subprocess
from .settings_updater import update_settings
from .url_creator import create_app_urls, update_project_urls
from .template_creator import create_templates
from .view_creator import create_home_view
from .superuser_creator import create_superuser
from colorama import Fore, Style
import sys

def print_progress(message):
    print(Fore.BLUE + message + Style.RESET_ALL)

def print_success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def create_django_project(project_name, app_name, use_tailwind, username, password):
    try:
        print_progress("Creating the Django project...")
        subprocess.run(['django-admin', 'startproject', project_name], check=True)

        os.chdir(project_name)
        print_progress("Creating the Django app...")
        subprocess.run([sys.executable, 'manage.py', 'startapp', app_name], check=True)

        print_progress("Creating necessary directories for static, media, and templates...")
        for directory in ['templates', 'static', 'media']:
            os.makedirs(directory, exist_ok=True)

        print_progress("Updating settings and URLs...")
        update_settings(project_name, app_name)
        create_app_urls(app_name)
        update_project_urls(project_name, app_name)

        print_progress("Creating templates and views...")
        create_templates(app_name, project_name, use_tailwind)
        create_home_view(app_name)

        print_progress("Running migrations...")
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)

        print_progress("Creating the superuser...")
        create_superuser(username, password)

        print_success(f'Django project "{project_name}" created successfully with app "{app_name}" and superuser "{username}".')

    except FileNotFoundError:
        print_error("Error: 'django-admin' command not found. Is Django installed?")
    except ValueError as ve:
        print_error(f"Input error: {ve}")
    except Exception as e:
        print_error(f"An unexpected error occurred: {e}")
