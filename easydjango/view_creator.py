import os

def create_home_view(app_name):
    views_content = """from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
"""
    with open(os.path.join(app_name, 'views.py'), 'w') as views_file:
        views_file.write(views_content)
