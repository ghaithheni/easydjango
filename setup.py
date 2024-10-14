from setuptools import setup, find_packages

setup(
    name='easydjango',
    version='0.1',
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
)
