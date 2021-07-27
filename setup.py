from setuptools import setup

setup(
    name='bookmarks2markdown',
    version='1.1.0',
    author='Nikola Trubitsyn',
    author_email='nikola.trubitsyn@gmail.com',
    url='https://github.com/trubitsyn/bookmarks2markdown',
    license='Apache License, Version 2.0',
    python_requires='>=3.6',
    long_description_content_type='text/markdown',
    description='Convert HTML bookmarks to Markdown',
    long_description=open('README.md').read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['bookmarks2markdown'],
    install_requires=[
        'netscape-bookmarks-file-parser @ git+https://github.com/FlyingWolFox/Netscape-Bookmarks-File-Parser.git@v1.1',
    ],
    entry_points={
        'console_scripts': [
            'bookmarks2markdown = bookmarks2markdown.__main__:main'
        ]
    },
)
