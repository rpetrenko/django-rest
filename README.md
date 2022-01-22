# django-rest

# run postgres container
* build image
```
docker build -t django-rest-db ./
```
* run postgres container
```
docker run -d --name django-rest-pg -p 5432:5432 -v `pwd`/pg_database:/var/lib/postgresql/data django-rest-db
```
* login to container and check database was created
```
docker run -it dango-rest-pg bash
psql -h localhost -U postgres -W mydatabase
(at prompt enter mypassword)
\l
\q
exit
```

# dev notes
* start project
```
django-admin startproject booktime .
```
* add new app
```
python manage.py startapp main
```
* don't forget to add app into settings.py INSTALLED_APPS

* constants in settings.py are accessible anywhere in the project by importing django.conf.settings.

* every time you change settings.py, the application has to be redeployed

