# wanted_pre_onboarding

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy wanted_pre_onboarding

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

## Directory Structure

```
wanted_pre_onboarding
├─ .editorconfig
├─ .git
├─ .gitattributes
├─ .gitignore
├─ .pre-commit-config.yaml
├─ .pylintrc
├─ .readthedocs.yml
├─ config
│  ├─ settings
│  │  ├─ base.py
│  │  ├─ local.py
│  │  ├─ production.py
│  │  ├─ test.py
│  │  └─ __init__.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ CONTRIBUTORS.txt
├─ docs(dir)
├─ LICENSE
├─ locale
│  └─ README.rst
├─ manage.py
├─ pytest.ini
├─ README.md
├─ requirements
│  ├─ base.txt
│  ├─ local.txt
│  └─ production.txt
├─ setup.cfg
├─ utility
└─ wanted_pre_onboarding
   ├─ conftest.py
   ├─ contrib
   │  └─ __init__.py
   ├─ posts
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ tests
   │  │  ├─ test_views.py
   │  │  └─ __init__.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  ├─ views.py
   │  └─ __init__.py
   ├─ static
   │  ├─ css
   │  │  ├─ posts
   │  │  │  ├─ base.css
   │  │  │  └─ header.css
   │  │  └─ project.css
   │  ├─ fonts
   │  │  └─ .gitkeep
   │  ├─ images
   │  │  └─ favicons
   │  │     └─ favicon.ico
   │  └─ js
   │     └─ project.js
   ├─ templates
   │  ├─ 403.html
   │  ├─ 404.html
   │  ├─ 500.html
   │  ├─ account(dir)
   │  ├─ base.html
   │  ├─ pages
   │  │  ├─ about.html
   │  │  └─ home.html
   │  ├─ posts
   │  │  ├─ base.html
   │  │  ├─ header.html
   │  │  ├─ index.html
   │  │  └─ product_create.html
   │  └─ users
   │     ├─ main.html
   │     ├─ user_detail.html
   │     └─ user_form.html
   ├─ users
   │  ├─ adapters.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ context_processors.py
   │  ├─ forms.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  │  ├─ 0002_auto_20220413_1536.py
   │  │  └─ __init__.py
   │  ├─ models.py
   │  ├─ tests
   │  │  ├─ factories.py
   │  │  ├─ test_admin.py
   │  │  ├─ test_forms.py
   │  │  ├─ test_models.py
   │  │  ├─ test_urls.py
   │  │  ├─ test_views.py
   │  │  └─ __init__.py
   │  ├─ urls.py
   │  ├─ views.py
   │  └─ __init__.py
   ├─ utils
   │  ├─ storages.py
   │  └─ __init__.py
   └─ __init__.py

```