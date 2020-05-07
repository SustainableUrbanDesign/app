# Sustainable Urban design

Prototype toolkit for sustainable urban design at the speed of thought.

# Setting up

If you wish to keep the project's python environment separate from your global environment, you should create a [virtual environment](https://docs.python.org/3/library/venv.html)

```
python3 -m venv env
source env/bin/activate
```

Use pip to install the requirements:

```
pip install -r requirements.txt
```

Move into the Django folder and create a new super user account:

```
cd sustainable_urban_design_space
./manage.py createsuperuser
Username: *your username*
Email address: *your email*
Password: *your password*
Password (again): *your password*
```

It may warn you if you use a password that is similar to your user name, or if it's too short or too common. You can bypass this warning by typing `Y` and then Enter. It doesn't matter in a development environment, but be sure to use secure credentials when deploying in production.

# Running the server

## Migrations

Before you can run the project, you will need to set up the database by running the migrations:

```
./manage.py migrate
```

## Starting the server

You can run the server with

```
./manage.py runserver
```

The server will now tell you that it's runnning on http://127.0.0.1:8000/

You can connect to the admin interface at http://127.0.0.1:8000/admin with your newly created superuser account.
