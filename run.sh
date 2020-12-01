#!/usr/bin/env bash

echo -e "\n##########################\nInstalling requirements...\n##########################\n"

pip3 install pipenv
pipenv install --ignore-pipfile

echo -e "\n##################\nStarting server...\n##################\n"

pipenv run uwsgi uwsgi.ini