# REST API for Call Records

This project is an application that offers an API to handle call records

## Getting Started

These instructions will get you a copy of the project up and running on your local machine
 for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

* Python 3.6+
* Postgre 10+
* Heroku free account


### Installing

A step by step series to get a development env running

Clone de project
```
$ git clone https://github.com/cnlenzc/call_records.git
```

Create a Python virtualenv and install dependencies from Pipfile
```
$ cd call_records
$ pipenv install --dev
$ pipenv shell
```

Create the database and user on PostgreSQL
```
database name: db_call_records
user: u_call_records
password: pwd123
privileges: can login=yes; create database=yes
```

Set environment variables by create .env file
```
cp .env_dev .env
```
Example of call_records/.env file for dev:
```
DEBUG=True
WEB_CONCURRENCY=2
DATABASE_URL='postgresql://u_call_records:pwd123@localhost:5432/db_call_records'
SECRET_KEY=")z*j%sx=d3zq9h_m-ovw-hq!p2()yzg!ydft_+smpw=#n(l0h*"
```

Create the database objects
```
$ python manage.py migrate
```

## Running the automatic tests

How to run the automated tests for this system
```
$ python manage.py test
```
Result
```
Loading .env File
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.............
----------------------------------------------------------------------
Ran 13 tests in 0.159s

OK
Destroying test database for alias 'default'...
```

## Running on local web server
```
$ python manage.py runserver
  para usar o server: WSGIServer/0.2 CPython/3.6.4
    ou 
$ heroku local
  para usar o server: gunicorn/19.7.1
```
Abra o browser com url
http://localhost:8000/call/ (WSGIServer)
 ou
http://localhost:5000/call/ (gunicorn)


## Using the API
You can use the API by internet with these URL

###### API Documentation
https://call_records-lenz.herokuapp.com/docs

###### Hello World page
https://call_records-lenz.herokuapp.com

###### Lista Agendamentos
https://call_records-lenz.herokuapp.com/call/


### Coding style tests

Using flake8 to check the coding style
```
$ flake8 . --count
```

The flake 8 checks:
	source files for errors (pyflakes).
	style conventions in PEP 8 (pycodestyle).
	code complexity (mccabe).

Using pylint to check the coding style
```
$ pylint --load-plugins pylint_django call_records/app
```


## Deployment by heroku

How to deploy this on a live system
```
$ git add .
$ git commit -m "Added a file"
$ heroku login
    Enter your Heroku credentials…
$ heroku apps:create call-records-lenz
    Creating ⬢ call-records-lenz... done
    https://call-records-lenz.herokuapp.com/ | https://git.heroku.com/call-records-lenz.git
$ git push heroku master
    -----> Python app detected
    -----> Launching... done, v7
$ heroku run python call_records/manage.py migrate
$ heroku config:set DEBUG=False
$ heroku config:set SECRET_KEY=')z*j%sx=d3zq9h_m-ovw-hq!p2()yzg!ydft_+smpw=#n(l0h*'
```

## Built With

* [Python](https://www.python.org) - The programming language used
* [Django](https://www.djangoproject.com) - The web framework used
* [Django Rest Framework](http://www.django-rest-framework.org) - The API REST framework used
* [Postgres.app](http://postgresapp.com/documentation/) - The SQL DataBase used
* [Heroku](https://devcenter.heroku.com/categories/python) - Used to deploy and cloud

## Authors

* **Carlos Neves Lenz Cesar** - *Initial work*

## License

MIT License

## Acknowledgments

* OList
* Heroku Docs
* Rest Django Framework Docs
* Django Docs
* You, who have read this document to the end
