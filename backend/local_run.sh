#!/bin/env sh

. venv/bin/activate

export FLASK_APP=e2e_messenger
export FLASK_ENV=development
export FLASK_DEBUG=1

flask run
