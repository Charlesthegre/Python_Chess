from setuptools import setup, find_packages

setup(
    name='Python_Chess',
    version='1.0.0',
    description='A Python-based chess game with drag-and-drop functionality using Pygame.',
    author='Haydan',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pygame>=2.5.2',
    ],
    entry_points={
        'console_scripts': [
            'Python_Chess=main:main',
        ],
    },
)
