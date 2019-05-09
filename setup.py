from codecs import open
from os.path import abspath, dirname, join
from setuptools import setup

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='socialist',
    long_description = long_description,
    url='https://github.com/OverwatchHeir/SociaList',
    download_url = 'https://github.com/OverwatchHeir/SociaList/archive/master.zip',
    install_requires=['tdqm', 'phonenumbers', 'validate_email', 'py3dns'],
    entry_points={
        'console_scripts': [
            'socialist=socialist:main',
        ],
    },

)
