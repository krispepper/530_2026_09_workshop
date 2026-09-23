#!/bin/bash

# Purpose: Automated shell script to activate the virtual environment, verify testing dependencies, and execute the test suite.

# Exit immediately if any command exits with a non-zero (error) status
set -e

# Activate the Python virtual environment
source .venv/bin/activate

# Ensure pytest is installed quietly without cluttering terminal output
pip install -q pytest

# Run all unit tests in verbose mode while setting the Python path to the root directory
PYTHONPATH=. pytest -v

# Print success message once tests have finished running
echo "All tests completed!"