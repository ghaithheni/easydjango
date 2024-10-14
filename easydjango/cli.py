from .project_setup import create_django_project
from colorama import init, Fore, Style
import getpass

init(autoreset=True)

def print_success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def print_warning(message):
    print(Fore.YELLOW + message + Style.RESET_ALL)

def print_info(message):
    print(Fore.BLUE + message + Style.RESET_ALL)

def interactive_prompt():
    print_info("Welcome to the EasyDjango Project Setup!")
    project_name = input(Fore.CYAN + "Enter the name of your Django project (default: myproject): " + Style.RESET_ALL) or "myproject"
    app_name = input(Fore.CYAN + "Enter the name of your Django app (default: myapp): " + Style.RESET_ALL) or "myapp"
    username = input(Fore.CYAN + "Enter the superuser username (default: admin): " + Style.RESET_ALL) or "admin"
    password = getpass.getpass(Fore.CYAN + "Enter the superuser password (default: admin): " + Style.RESET_ALL) or "admin"
    return project_name, app_name, username, password

def main():
    project_name, app_name, username, password = interactive_prompt()
    try:
        create_django_project(project_name, app_name, False, username, password)
    except Exception as e:
        print_error(f"Error during project setup: {e}")

if __name__ == '__main__':
    main()
