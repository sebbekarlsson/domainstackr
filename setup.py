import os
from setuptools import setup


setup(
    name='domainstackr',
    version='1.0',
    description='Domain Name Scraper',
    author='Sebastian Robert Karlsson',
    author_email='sebbekarlsson97@gmail.com',
    url='http://www.ianertson.com/',
    install_requires=[
        'flask',
        'flask-wtf',
        'wtforms',
        'pymongo',
        'pytest',
        'pytest-cov'
    ]
)
