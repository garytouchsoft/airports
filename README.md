# Airport lookup

## Setup Steps

python -m venv .env
source .env/bin/activate
cd [project root]
pip install -r requirements.txt
python manage.py runserver


## Contents

Main search page:
http://127.0.0.1:8000/

Searching is performed using the haversine formula
https://en.wikipedia.org/wiki/Haversine_formula


Admin:
http://127.0.0.1:8000/admin
l: admin
p: asd$fdd%6dgNMbvFwvc

Airports can be imported via CSV


## Docker

To run in a Docker container:
sudo docker-compose up












