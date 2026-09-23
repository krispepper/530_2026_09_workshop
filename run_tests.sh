set -e
source .venv/bin/activate
pip install -q pytest
PYTHONPATH=. pytest -v