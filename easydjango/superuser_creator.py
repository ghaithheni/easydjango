import django
import os
import sys

def setup_django():
    current_dir = os.getcwd()
    project_name = os.path.basename(current_dir)

    settings_module = f"{project_name}.settings"
    
    sys.path.append(current_dir)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    django.setup()

def create_superuser(username, password):
    try:
        setup_django()
        
        from django.contrib.auth import get_user_model
        User = get_user_model()

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(
                username=username,
                email="admin@example.com",
                password=password
            )
            print(f'Superuser "{username}" created successfully.')
        else:
            print(f'Superuser "{username}" already exists.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
