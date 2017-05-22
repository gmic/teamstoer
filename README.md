# teamstoer

teamstoer.nl website

# TODO

Design:

- Event layout: using Streamfield block with events
- Hide header when scrolling


Tech:

- Backup website content **
- Build js with gulpfile
- Restore content in dev env
- Use video plugin
- Use mechanisms from ansible-multi-django (multi app)

# Running gulp

cd teamstoer/static/base_theme
npm install
gulp


# Getting started

Install postgress.

Create the user and database in postgress:

    createuser --pwprompt teamstoer-dev
    createdb -Oteamstoer-dev -Eutf8 teamstoer-dev

Create schema's:

    ./manage.py migrate

Run the server:

    ./manage.py runserver
