# Welcome to 'Know Your Zodiac'
[![Build Status](https://travis-ci.org/VincentWen/know-your-zodiac.svg?branch=master)](https://travis-ci.org/VincentWen/know-your-zodiac)

##Introduction
*Do you want to know which animal are you in Chinese Zodiac (A.K.A East Zodiac)?*

*Do you want to know which constellation are you in Western astrology (A.K.A West Zodiac)?*

Type in your birthday (year, month and day), 'Know Your Zodiac' will return your East&West Zodiac sign.

##How to deploy it
###Local

Follow the instruction(bash in OS X):
* virtualenv venv
* pip install -r requirements.txt
* python runserver.py
* visit localhost:5000

###Heroku

Procfile and requirements.txt are ready. Follow the [instruction of how to deploy python to Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) and replace its example to this Github repository.

##How to use API
###RESTful API
It accepts both GET and POST method. The entry is http://[yourpage]/api/ . The parameters are **year**, **month** and **day**.

###JSON
It returns **status = 1** when it succeeds. Inside the **data**, it includes **birthday**, **eastZodiac** and **westZodiac**.

In both the zodiac entries, **number** stands for the order of the sign, **name** stands for the name of the sign, and **imageurl** represents the url of the sign's image.

It returns **error** entry with error information when it fails.

##Database
It applies either MySQL and SQLite as database. I recommend to use SQLite as tryout, as my MySQL server might be closed in near future.

If you want to use your own database server, change the url in 'config.py'. Import the database from 'deploy/schema.sql'.

##Development

* Python/Flask
* Bootstrap
* jQuery/Ajax

##Demo
* [https://your-zodiac-2016.herokuapp.com/](https://your-zodiac-2016.herokuapp.com/)
* [https://your-zodiac-2016.herokuapp.com/api/?year=1955&month=2&day=24](https://your-zodiac-2016.herokuapp.com/api/?year=1955&month=2&day=24)

*Deployed on 11th October 2016, it might get expired at any moment*
