#!/bin/bash
# flask settings
gunicorn --bind 0.0.0.0:5123  webserver:app