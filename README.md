Django website for my sister
============================

Written based on the requirements of her business as well as giving me the ability to code a django project from the ground up.

Stuff to do:
- Allow portraits to re refreshed via management command.
- Create review pictures.
- Polish pages.
- Add footer.


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