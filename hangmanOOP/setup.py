import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hangman",
    version="0.0.3",
    author="Jordan Diaz",
    author_email="jordandiaz1993@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jordandiazfr/hangman-oop",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['hangman=hangmanGame.main:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)