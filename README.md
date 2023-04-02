# Chronus API

API project for **Chronus**, application that helps you manage your time.

## Prerequisites

Make sure you have installed these:
- [Python 3.8.0]('https://www.python.org/downloads/release/python-380/') - Python is an interpreted, high-level and general-purpose programming language.
- [PostgreSQL 12]('https://www.postgresql.org/download/') - PostgreSQL is a powerful, open source object-relational database system.

## Installation

Clone the project and go to the folder of project

```shell script
git clone git@github.com:creadordlx/chronus_backend.git
```

Install **pipenv**

```shell script
pip install pipenv
```

Activate **pipenv** virtual environment

```shell script
pipenv shell
```

Install required **python modules**

```shell script
pipenv install --dev
```

Create **database** in **PostgreSQL** and save its name. You can create **User** for this database
(default postgres user can be used as well). 

Make a copy of **.env.example** and name it **.env**

```shell script
cp .env.example .env
```

Change required values in **.env**

```shell script
DB_NAME = <db_we_just_created>
DB_USER = <user_with_access_to_this_db>
DB_PASSWORD = <password>
DB_HOST = localhost
DB_PORT = 5432
```

> Values of `DB_HOST` and `DB_PORT` should be like this by default, unless you changed it yourself.

Run **Django migrations**

```shell script
./manage.py migrate
```

> On **Windows**, `./` at the is not needed, use `manage.py <command>`

Create **superuser**.

```shell script
./manage.py createsuperuser
```

It will ask for `email` and `password`

Now you are set up!

## Running

Go to the folder with project and activate pipenv

```shell script
pipenv shell
```

Run the app

```shell script
./manage.py runserver
```

### Authors
- Adi Sabyrbayev [Github](https://github.com/Madrigals1), [LinkedIn](https://www.linkedin.com/in/madrigals1/)
- Aibek Ziyashev [Github](https://github.com/dmndcrow), [LinkedIn](https://www.linkedin.com/in/dmndcrow)