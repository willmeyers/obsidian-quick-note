from setuptools import setup, find_packages

setup(
    name="quick-note",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'quick-note=quick_note:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to quickly add notes to Obsidian daily notes",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/quick-note",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
