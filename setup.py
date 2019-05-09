from codecs import open
from os.path import abspath, dirname, join
from setuptools import setup
from socialist import __version__, __author__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='socialist',
    version=__version__,
    long_description = long_description,
    url='https://github.com/OverwatchHeir/SociaList',
    download_url = 'https://github.com/OverwatchHeir/SociaList/archive/master.zip',
    author=__author__,
    author_email='overwatchheir@protonmail.com',
    install_requires=['tdqm', 'phonenumbers', 'validate_email', 'py3dns'],
    entry_points={
        'console_scripts': [
            'socialist=socialist:main',
        ],
    },

)
