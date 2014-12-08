========
Eulasees
========

Team Bermuda's valiant attempt at making reading Eula's fun.  

Since the average EULA is about as easy to read as the classic, James
Joyce' Ulysees we took the liberty of borrowing the name.

The plan
========

The idea was to create a site where people can upload and annotate
EULA's.

EULA's can be split into *snippets* of text and tags applied to those
snippets.

Each tag tries to explain what the EULA means in plain language.

Once a EULA has been processed like this a simple display is available
to see what the EULA really means.

Once we have a bunch of tagged EULA's then we can have some fun.

Let people explore which services have which clauses.

Create a quiz to see if people can guess which egregious term of use
comes from which EULA.

Tools used
==========

Django was used to build a restful API, along with
`django-rest-framework`_

The API is documented using `django-rest-swagger`_

The rest of the application is written with `angular.js`_

Where we are at
===============

Of course, everything works just perfectly on our machines.  

As of an hour before the end of the hackathon things are in bits.

We have a working restful API.  

We have a nice angular app that works just fine with pre-canned data.

The only tiny problem is the angular app is unable to talk to the API.

*curl* can talk to the API, the swagger interface can make calls, but
sadly the one piece of code that we would really like to work is
failing :(

One hour to go. 

STOPPRESS: django-cors-headers to the rescue :)

.. _django-rest-swagger: http://django-rest-swagger.readthedocs.org/en/latest/

.. _django-rest-framework: http://www.django-rest-framework.org/
