# Weather alerting system for logistic companies
This program allow the company to monitor their truck in order to be aware of high wind speed and other possible natural causes

## Setting up

- install python and docker
- `pip install poetry`
- `poetry install`


## Running the server

- `docker run -d -p 6379:6379 redis`
- `docker run -e MYSQL_ROOT_PASSWORD=pwd -d -p 3306:3306 mysql`
- `celery -A core worker --loglevel=info`
- `celery -A core beat`
- `poetry run python manage.py runserver`


## Todo

- Test the Open Weather Map api and set up for development (DONE)
- Test the Samsara api and set up for development (DONE)
- Crate models for truck (DONE)
- Set up background worker - Celery (DONE)
- Set up MySQL (ERROR)
- Code scripts to easily set up and run the app
- Dockerize the app using Docker