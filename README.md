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
SECRET_KEY="**************************************************"
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
DEBUG=True
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............................................
----------------------------------------------------------------------
Ran 44 tests in 0.789s

OK
Destroying test database for alias 'default'...

Process finished with exit code 0
```

## Running on local web server
```
$ python manage.py runserver
  server: WSGIServer/0.2 CPython/3.6.4
    or
$ heroku local
  server: gunicorn/19.7.1
```
Open in browser
http://localhost:8000/ (WSGIServer)
 ou
http://localhost:5000/ (gunicorn)


## Coding style tests

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
    -----> Launching...
           Released v6
           https://call-records-lenz.herokuapp.com/ deployed to Heroku
    Verifying deploy... done.
$ heroku run python call_records/manage.py migrate --app call-records-lenz
$ heroku config:set DEBUG=False --app call-records-lenz
$ heroku config:set SECRET_KEY='**************************************************' --app call-records-lenz
$ heroku run python call_records/manage.py create_data --app call-records-lenz
```

## Using the API
You can use the API by internet with these URL

###### Welcome/index page
https://call-records-lenz.herokuapp.com

###### API Documentation
https://call-records-lenz.herokuapp.com/docs

###### Charge price setting
https://call-records-lenz.herokuapp.com/config-price

###### Calls handle
https://call-records-lenz.herokuapp.com/call-record

###### Create/retrieve the bill
https://call-records-lenz.herokuapp.com/bill

## Use case

Example charge price setting
```
{
    "start_time": 6,
    "end_time": 22,
    "price_per_call_standard": "0.36",
    "price_per_call_reduced": "0.36",
    "price_per_minute_standard": "0.09",
    "price_per_minute_reduced": "0.00"
}
```

Example call-record list with filter call_id=9
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 63,
            "type": "1",
            "timestamp": 1518299833,
            "call_id": 9,
            "source": "1632203625",
            "destination": "21980000007"
        },
        {
            "id": 64,
            "type": "2",
            "timestamp": 1518300656,
            "call_id": 9,
            "source": null,
            "destination": null
        }
    ]
}
```

Example bill of phone number 1632203625 and period 2018-02
```
{
    "id": 6,
    "source": "1632203625",
    "period": "2018-02",
    "calls": [
        {
            "destination": "21980000007",
            "start_date_time": "2018-02-10T21:57:13",
            "duration": "00:13:43",
            "price": "0.54"
        }
    ]
}
```

## Built With

* [Python 3.6.4](https://www.python.org) - The programming language used
* [Django 2.0.2](https://www.djangoproject.com) - The web framework used
* [Django Rest Framework 3.7.7](http://www.django-rest-framework.org) - The API REST framework used
* [Postgres 2.1.2 PostgreSQL 10](http://postgresapp.com/documentation/) - The SQL DataBase used
* [Heroku](https://devcenter.heroku.com/categories/python) - Used to deploy and cloud

Development environment

* MacBook with MacOS 10.13.3
* PyCharm 2017.3.4 (Community Edition)

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

