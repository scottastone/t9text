#!/bin/bash

# Check if we are in the venv
if [[ "$VIRTUAL_ENV" == "" ]]; then
    source .venv/bin/activate
fi

# Build the project and then remove the build folder
pyinstaller --onefile t9text.py
rm -rf build