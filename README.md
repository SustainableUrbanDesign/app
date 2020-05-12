# Sustainable Urban design
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://maxthakur.com"><img src="https://avatars1.githubusercontent.com/u/25856189?v=4" width="100px;" alt=""/><br /><sub><b>Max Thakur</b></sub></a><br /><a href="#translation-MaxThakurCodes" title="Translation">🌍</a> <a href="https://github.com/SustainableUrbanDesign/app/commits?author=MaxThakurCodes" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Nowserep"><img src="https://avatars3.githubusercontent.com/u/65257460?v=4" width="100px;" alt=""/><br /><sub><b>Nowserep</b></sub></a><br /><a href="#translation-Nowserep" title="Translation">🌍</a></td>
    <td align="center"><a href="https://bryliechristopheroxley.info"><img src="https://avatars1.githubusercontent.com/u/17307?v=4" width="100px;" alt=""/><br /><sub><b>Brylie Christopher Oxley</b></sub></a><br /><a href="https://github.com/SustainableUrbanDesign/app/commits?author=brylie" title="Code">💻</a> <a href="#projectManagement-brylie" title="Project Management">📆</a> <a href="https://github.com/SustainableUrbanDesign/app/issues?q=author%3Abrylie" title="Bug reports">🐛</a> <a href="https://github.com/SustainableUrbanDesign/app/commits?author=brylie" title="Documentation">📖</a> <a href="#ideas-brylie" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/SustainableUrbanDesign/app/pulls?q=is%3Apr+reviewed-by%3Abrylie" title="Reviewed Pull Requests">👀</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!