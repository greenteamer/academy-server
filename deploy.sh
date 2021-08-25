#!/bin/bash
APP_DIR=$(dirname $(readlink -f $0))
ENV_DIR=$(dirname $APP_DIR)

# python_env="/.env/bin/python3"
$ENV_DIR/.env/bin/python3 -m pip install -r deps.pip
$ENV_DIR/.env/bin/python3 $APP_DIR/manage.py migrate
$ENV_DIR/.env/bin/python3 $APP_DIR/manage.py collectstatic
