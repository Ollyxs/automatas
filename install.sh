#!/bin/bash

pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
