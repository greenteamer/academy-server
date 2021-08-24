#!/bin/sh
../.env/bin/python3 -m pip install -r deps.pip
../.env/bin/python3 -m manage.py migrate
