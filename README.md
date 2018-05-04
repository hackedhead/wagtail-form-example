wagtail-form-example
====================

An example of implementing a Django form on a Wagtail site, without using the 'wagtailforms' module

## This fork demonstrates a bug

The models in this fork are designed to reproduce an error where a set of model files and wagtail_hooks customizations cause a circular import problem that exhibits under wagtail 1.12 but not under wagtail 1.11.

Steps:


* clone repo
* pip install -r requirements
* python manage.py runserver
* pip install wagtail==1.12
* python manage.py runserver
