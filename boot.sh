#!/bin/bash
gunicorn -D -b :5001 --access-logfile - --error-logfile - --certfile=${CERT:-/tls/cert} --keyfile=${KEY:-/tls/key} admissions-webhook:app
gunicorn -D -b :5000 --access-logfile - --error-logfile - admissions-webhook:app
tail -f /var/log/faillog

