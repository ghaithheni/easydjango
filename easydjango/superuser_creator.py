import subprocess
import sys

def create_superuser(username, password):
    try:

        subprocess.run([
            sys.executable, 'manage.py', 'createsuperuser', 
            '--noinput', 
            f'--username={username}', 
            f'--email=admin@example.com'
        ])

        subprocess.run([sys.executable, 'manage.py', 'shell', '-c', 
            f'from django.contrib.auth import get_user_model; '
            f'User = get_user_model(); '
            f'User.objects.filter(username="{username}").update(password="{password}")'
        ], check=True)

    except subprocess.CalledProcessError as e:
        print(f'Error creating superuser: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
