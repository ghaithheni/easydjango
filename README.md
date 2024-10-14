# Easy Django Project Setup Tool

EasyDjango is a command-line tool for quickly setting up a new Django project with customizable options, including app creation, templates, static files, and superuser setup.

## Features

- Create a new Django project and app with minimal commands.
- Optionally include Tailwind CSS for styling (by adding the argument `--tailwind`).
- Automatic creation of necessary directories for templates, static files, and media.
- Create a superuser during setup.
- Colorful and user-friendly CLI prompts.

## Installation

You can install QuickDjango via pip. First, ensure you have Python and pip installed, then run:

```bash
pip install easydjango-project
```

> **Note**: The installation command is the same for Windows, macOS, and Linux, but you might need to use pip3 instead on some operating systems.

## Usage

To create a new Django project, execute the following easy command:

```bash
easydjango
```

You will be prompted to provide the following information:

Project Name (default: `myproject`)
App Name (default: `myapp`)
Superuser Username (default: `admin`)
Superuser Password (default: `admin`)


## Example Interaction
```bash
Welcome to the EasyDjango Project Setup! 
Enter the name of your Django project (default: myproject): 
Enter the name of your Django app (default: myapp): 
Enter the superuser username (default: admin): 
Enter the superuser password (default: admin): 
```

## Contributing

If you'd like to contribute to EasyDjango, feel free to fork the repository and submit a pull request. Any contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Acknowledgements

Django for being an awesome web framework.
Colorama for colorful terminal text.

## Contact

For inquiries or feedback, please reach out at [elghaithheni@gmail.com](mailto:elghaithheni@gmail.com).