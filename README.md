# django-addresses
Simple addressbook app using django.
Demo for use with `django` `runserver`,
not a deployment ready project.

## Features

- list organisations and people
- allow the user to see the names and contact details of people in organisations
- user can manage the people who are in an organisation.
- each organisation should have a name and contact details
- organisations and people can be created, edited and deleted.

## Setup
assuming a `python` environment
with

```shell
$ python --version
3.5.2
```
then
```shell
$ pip install requirements.txt
```

or, for development tools:
```shell
$ pip install requirements_dev.txt
```
## Usage
from the folder containg `manage.py` run

```shell
$ python manage.py migrate
$ python manage.py runserver
```
and point a browser at `http://localhost:8000/`

## History
I tried to do this TDD style inspired by
Harry Percival's [TestingGoat book](http://www.obeythetestinggoat.com/).
Unfortunately, I ran out of Django knowledge to carry on
down that path.

My TDD attempts are on [GitHub](https://github.com/lbillingham/borked-tdd-django-contacts) for reference.
