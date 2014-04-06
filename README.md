Django website for my sister
============================

About
-----

My sister is a makeup artist and currently uses a cheesy make-it-yourself website. I agreed to make one for her and customize it to her liking. This is the result.

Aditionally, I made all of the often chaning elements (pictures and reviews) managable through the admin.


Setup
-----

Install your JS dependencies with Node:

    $ npm install

Install your front-end libraries with Grunt/Bower:

	$ npm install -g bower

    $ bower install

    $ npm install -g grunt-cli

    $ grunt

Install python requirements

    $ pip install -r ./requirements.txt

Start the app

    $ python manage.py runserver 8000


Requirements
------------

* python 2.7
* Ruby and the sass gem
* a mail server running (e.g. sendmail on ubuntu)
* pip
* NodeJs
