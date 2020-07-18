# Sustainable Urban design
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

[![Open Collective](https://badgen.net/opencollective/backers/suds)](https://opencollective.com/suds)
[![Youtube](https://img.shields.io/badge/dynamic/json?label=Youtube&color=brightgreen&query=items[0].statistics.subscriberCount&url=https%3A%2F%2Fwww.googleapis.com%2Fyoutube%2Fv3%2Fchannels%3Fpart%3Dsnippet%252CcontentDetails%252Cstatistics%26id%3DUCrV_KSms3BNStyOFAvx4l1w%26key%3DAIzaSyB2IsPIY-XsnJBwgMaWIZMBROZ283LA29g)](https://www.youtube.com/channel/UCrV_KSms3BNStyOFAvx4l1w)
[![License](https://img.shields.io/badge/license-GNU-brightgreen)](/LICENSE)
[![Riot](https://img.shields.io/badge/Chat-Join%20our%20discussion%20on%20Matrix-brightgreen)](https://riot.im/app/#/room/#sud:matrix.org)
[![Twitter](https://badgen.net/twitter/follow/SustUrbanDesign)](https://twitter.com/SustUrbanDesign)

## Table of Contents

* [Installation](#installation)
* [Support](#support)
* [Social Media Links](#links)
* [License](#license)

## What is this?

This project is an open-source, prototype toolkit for sustainable urban design. Go check out our [website](https://sustainableurbandesign.space/).
To stay updated about progress and events in the community, follow us on [Twitter](https://twitter.com/SustUrbanDesign) and subscribe to our [YouTube channel](https://www.youtube.com/channel/UCrV_KSms3BNStyOFAvx4l1w).
To chat with community members, check out [Matrix/Riot](https://riot.im/app/#/room/#sud:matrix.org), and if you'd like to support the project financially you can do so on [OpenCollective](https://opencollective.com/suds).

Below, you can see a user-interface mockup showing the main components of the toolkit.

![UrbanDesignSpace App UI mockup](design/UI-mockup.png)

## We need your help!

Our team would love for people to help out in anyway they can, right now we're looking for translators and anyone willing to help out.

## Installation

### Requirements

If you dont have the latest version of python then do download it from [here](https://www.python.org/downloads/)


### Environment
If you wish to keep the project's python environment separate from your global environment, you should create a [virtual environment](https://docs.python.org/3/library/venv.html)

```
python3 -m venv env
source env/bin/activate
```

### Python dependencies
Use [pip](https://pip.pypa.io/en/stable/installing/) to install the dependencies:

```
pip install -r requirements.txt
```


#### Move into the Project Folder:

```
cd platform
```
## Running the server

### Migrations


Before you can run the project, you will need to set up the database by running the migrations:

```
./manage.py migrate
```

### Create super user
Move into the Project Folder:
```
cd platform
```

Create a new super user account:
```
python manage.py createsuperuser

Username: *your username*
Email address: *your email*
Password: *your password*
Password (again): *your password*
```

It may warn you if you use a password that is similar to your user name, or if it's too short or too common. You can bypass this warning by typing `Y` and then Enter. It doesn't matter in a development environment, but be sure to use secure credentials when deploying in production.

### Starting the server

You can run the server with

```
python manage.py runserver
```

The server will now tell you that it's running on http://127.0.0.1:8000/

You can connect to the admin interface at http://127.0.0.1:8000/admin with your newly created superuser account.

## Support

* See [CONTRIBUTING.md](CONTRIBUTING.md)

## Resources

## Links
[Twitter](https://twitter.com/SustUrbanDesign)
[YouTube](https://www.youtube.com/channel/UCrV_KSms3BNStyOFAvx4l1w)
[OpenCollective](https://opencollective.com/suds)
[Riot/Matrix](https://riot.im/app/#/room/#sud:matrix.org)

## Contributors ✨

Thanks goes to these awesome people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://maxthakur.com"><img src="https://avatars1.githubusercontent.com/u/25856189?v=4" width="100px;" alt=""/><br /><sub><b>Max Thakur</b></sub></a><br /><a href="#translation-MaxThakurCodes" title="Translation">🌍</a> <a href="https://github.com/SustainableUrbanDesign/app/commits?author=MaxThakurCodes" title="Code">💻</a> <a href="https://github.com/SustainableUrbanDesign/app/pulls?q=is%3Apr+reviewed-by%3AMaxThakurCodes" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/SustainableUrbanDesign/app/commits?author=MaxThakurCodes" title="Documentation">📖</a> <a href="#ideas-MaxThakurCodes" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-MaxThakurCodes" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/Nowserep"><img src="https://avatars3.githubusercontent.com/u/65257460?v=4" width="100px;" alt=""/><br /><sub><b>Nowserep</b></sub></a><br /><a href="#translation-Nowserep" title="Translation">🌍</a></td>
    <td align="center"><a href="https://bryliechristopheroxley.info"><img src="https://avatars1.githubusercontent.com/u/17307?v=4" width="100px;" alt=""/><br /><sub><b>Brylie Christopher Oxley</b></sub></a><br /><a href="https://github.com/SustainableUrbanDesign/app/commits?author=brylie" title="Code">💻</a> <a href="#projectManagement-brylie" title="Project Management">📆</a> <a href="https://github.com/SustainableUrbanDesign/app/issues?q=author%3Abrylie" title="Bug reports">🐛</a> <a href="https://github.com/SustainableUrbanDesign/app/commits?author=brylie" title="Documentation">📖</a> <a href="#ideas-brylie" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/SustainableUrbanDesign/app/pulls?q=is%3Apr+reviewed-by%3Abrylie" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/pgrimaud"><img src="https://avatars1.githubusercontent.com/u/1866496?v=4" width="100px;" alt=""/><br /><sub><b>Pierre Grimaud</b></sub></a><br /><a href="https://github.com/SustainableUrbanDesign/app/commits?author=pgrimaud" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/jfinmaniv"><img src="https://avatars2.githubusercontent.com/u/15154823?v=4" width="100px;" alt=""/><br /><sub><b>John Inman</b></sub></a><br /><a href="https://github.com/SustainableUrbanDesign/app/commits?author=jfinmaniv" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rmk118"><img src="https://avatars1.githubusercontent.com/u/67233373?v=4" width="100px;" alt=""/><br /><sub><b>rmk118</b></sub></a><br /><a href="https://github.com/SustainableUrbanDesign/app/commits?author=rmk118" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!


# License

* see [GNU Affero General Public License v3.0](https://github.com/SustainableUrbanDesign/app/blob/master/LICENSE)
