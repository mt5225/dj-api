# dj-api

# migrate data from sqlite3 to mysql

1. Execute:
   `python manage.py dumpdata > datadump.json`

2. Next, change your settings.py to the mysql database.

3) Finally
   `python manage.py loaddata datadump.json`
