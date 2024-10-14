import os

def create_app_urls(app_name):
    urls_content = f"""from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
"""
    with open(os.path.join(app_name, 'urls.py'), 'w') as urls_file:
        urls_file.write(urls_content)

def update_project_urls(project_name, app_name):
    project_urls_path = os.path.join(project_name, 'urls.py')
    with open(project_urls_path, 'a') as urls_file:
        urls_file.write(f"\nfrom django.urls import include\n")
        urls_file.write(f"urlpatterns += [path('', include('{app_name}.urls'))]\n")
