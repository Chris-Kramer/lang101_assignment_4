#!/usr/bin/env bash

VENVNAME=as4-venv #Environment name

echo "Creating environment"
python -m venv $VENVNAME

# This makes sure that the bash script can be run from bash emulator on windows 
# Test if the folder bin in venvname exists
if [ -d "$VENVNAME/bin" ]

    then
        source $VENVNAME/bin/activate
        echo "Building venv for Linux/Mac ..."
    
    else
        source $VENVNAME/Scripts/activate
        echo "Building venv for Windows ..."
fi

# Upgrade pip

# I'm specifying that I'm using pip from python, since my pc have problems upgrading pip locally if I don't do it.
python -m pip install --upgrade pip

# Test if requirements exist and install it
test -f requirements.txt && python -m pip install -r requirements.txt


# Download en_core_web nlp model
python -m spacy download en_core_web_sm

#Move to src folder
cd src

echo "running script"
python assignment4-cmk.py $@

echo "deactivating and removing environment"
deactivate

# move back to parent dir
cd ..

# Remove virtual environment
rm -rf $VENVNAME

echo "Done! The centrality measures have been calculated and saved in a csv-file, and the network have been graphed"