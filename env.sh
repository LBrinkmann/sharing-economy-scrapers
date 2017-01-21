#!/bin/bash

set -e

python3.5 -m venv .venv
source .venv/bin/activate
pip install -U pip==8.0.2
pip install -U setuptools

pip install numpy==1.10.4
pip install scipy==0.16.0

pip install -e .
pip install -e ".[dev]"
