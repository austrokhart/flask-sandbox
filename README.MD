
# flask-sandbox

This project is a simple example of working with Flask framework and writing tests for it.

## Installation

To install run: <br>
`pip install -r requirements.txt`


After installation, you need to create configuration files in the following places:
* /config.py
* /blueprints/sessions/config.py

Examples will be located in same places.

To generate a secret key you can run: <br>
`python -c 'import os; print(os.urandom(16))'`

## Requests

To send a request you can run: <br>
`curl --request <type> --data "<param>=<value>&<param>=<value>" <url>`

## Testing

To test run: <br>
`python3 -m unittest tests.py`

