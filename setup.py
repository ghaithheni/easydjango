from setuptools import setup, find_packages

setup(
    name='easydjango-project',
    version='1.0.5',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'easydjango=easydjango.cli:main',
        ],
    },
    install_requires=[
        'Django>=4.2',
        'colorama',
    ],
    description='A CLI tool for quickly setting up Django projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ghaith Heni',
    author_email='elghaithheni@gmail.com',
    license='MIT',
    url='https://github.com/ghaithheni/easydjango',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
