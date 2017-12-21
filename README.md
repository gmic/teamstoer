# teamstoer

http://www.teamstoer.nl/ website

# Running gulp

npm install --global gulp-cli

cd teamstoer/static/base_theme
npm install
gulp


# Getting started

* Install python
* Install postgres

Create the user and database in postgres:

    createuser --pwprompt teamstoer-dev
    createdb -Oteamstoer-dev -Eutf8 teamstoer-dev

Create schema's:

    ./manage.py migrate

Run the server:

    ./manage.py runserver
