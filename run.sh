#!/bin/bash
pipenv run uwsgi --http :9090 --wsgi-file server.py