# Admissions Webhook Flask Server

A Kuberentes admissions controller webhook written in python for validating and mutating validations.

## Flask environment setup

Create a virtual environment  

```bash
virtualenv venv

# Install requirements
venv/bin/pip install -r requirements.txt

# Start the app for testing locally
venv/bin/python admissions-webhook.py
```

Access the app on port 5000 and try the API endpoints: 

- [http://localhost:5000/version](http://localhost:5000/version)
