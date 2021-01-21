#!/usr/bin/env bash 
echo Installing hangman
cd hangmanOOP
python setup.py install
cd ..
pip install hangmanOOP
hangman