import os

def update_settings(project_name, app_name):
    settings_path = os.path.join(project_name, 'settings.py')
    
    with open(settings_path, 'a') as settings_file:
        settings_file.write("import os\n")
        
        # Add the app to INSTALLED_APPS
        settings_file.write(f"\nINSTALLED_APPS.append('{app_name}')\n")
        
        # Add media settings
        settings_file.write("\nMEDIA_URL = '/media/'\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")
        
        # Add static settings
        settings_file.write("\nSTATIC_URL = '/static/'\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n")
        
        # Update the TEMPLATES setting to include the root templates directory
        settings_file.write(
            "\nTEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'templates'))\n"
        )
