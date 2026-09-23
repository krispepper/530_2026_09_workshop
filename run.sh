#!/bin/bash

# Purpose: Automation script to set up the virtual environment, install requirements, and launch the Flask application.

# Create a local Python virtual environment in the .venv folder
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install all required Python packages specified in the requirements file
pip install -r requirements.txt

# Start the Flask application
python3 app.py