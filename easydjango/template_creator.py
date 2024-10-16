import os

def create_templates(app_name, project_name, use_tailwind):
    templates_dir = os.path.join(app_name, 'templates')
    os.makedirs(templates_dir, exist_ok=True)

    tailwind_script = (
        '    <script src="https://cdn.tailwindcss.com"></script>\n' if use_tailwind else ''
    )

    base_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
{tailwind_script}</head>
<body>
{{% block content %}}
{{% endblock content %}}
</body>
</html>"""


    with open(os.path.join(templates_dir, 'base.html'), 'w', encoding='utf-8') as base_file:
        base_file.write(base_html_content)

    home_html_content = f"""{{% extends 'base.html' %}}

{{% block content %}}
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }}
        h1 {{
            color: #4A90E2;
        }}
        h2 {{
            color: #333;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background: #fff;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        a {{
            color: #4A90E2;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
        }}
    </style>
    <div class="container">
        <h1>Welcome to {project_name}!</h1>
        <p>Congratulations! You have successfully set up your Django project using <strong>EasyDjango</strong>.</p>
        
        <h2>What to Do Next:</h2>
        <ul>
            <li>Explore the <strong>views.py</strong> file in your app directory (<code>{app_name}/views.py</code>) to customize your application logic.</li>
            <li>Modify the <strong>urls.py</strong> file in your app (<code>{app_name}/urls.py</code>) to define your app's URL patterns.</li>
            <li>Edit the <strong>base.html</strong> file in the <code>templates</code> directory to change your site’s layout and design.</li>
            <li>Visit the <strong>admin panel</strong> by navigating to <code>/admin</code> after running the development server.</li>
            <li>Check the official <a href="https://www.djangoproject.com/">Django documentation</a> for more advanced features and customization options.</li>
        </ul>
        
        <h2>Need Help?</h2>
        <p>If you have any questions or need assistance, feel free to reach out at <a href="mailto:elghaithheni@gmail.com">elghaithheni@gmail.com</a>.</p>
    </div>
{{% endblock content %}}
"""

    with open(os.path.join(templates_dir, 'home.html'), 'w', encoding='utf-8') as home_file:
        home_file.write(home_html_content)
