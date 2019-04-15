#!/bin/bash
gunicorn -D -b :5001 --access-logfile app.log --error-logfile app.log --certfile=${CERT:-/tls/cert} --keyfile=${KEY:-/tls/key} admissions-webhook:app
gunicorn -D -b :5000 --access-logfile app.log --error-logfile app.log admissions-webhook:app
tail -f app.log