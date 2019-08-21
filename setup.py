from setuptools import setup, find_packages
from json import loads as parseJSON

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('package.json') as raw:
    manifest = parseJSON(raw.read())

with open('info.json', 'r') as text:
    info = parseJSON(text.read())

setup(
    name=manifest['name'],
    version=manifest['version'],
    author=manifest['author'],
    author_email=info['email'],
    description=manifest['description'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=manifest['repository']['url'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
    ]
)
