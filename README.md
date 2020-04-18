# heroku-polls-backend

This repo contains Python backend code and configuration files for Heroku.

## Local setup

To develop locally create `.env` file within `./src` directory and add following code to it:  
```
DEBUG=True
SECRET_KEY=<insert_secret_key_here>
ALLOWED_HOSTS=*,
```

Once container is up and running apply migrations (a one-time operation) and create superuser by executing:  
`docker ps` -> to list all running containers and retrieve id or name of running backend container  
`docker exec -it <id_or_name_of_running_container> /bin/bash` -> to enter the container  
`python manage.py migrate` -> to execute migrations  
`python manage.py createsuperuser` -> to create superuser  
`exit` -> to exit the container  

Test review app

## create db
- create user polls with password 'test1234' SUPERUSER;
- create database polls with owner polls;


https://thinkster.io/tutorials/django-json-api/authentication

https://github.com/chase2981/conduit-django/blob/09-filtering/conduit/apps/articles/serializers.py

https://django-rest-framework-json-api.readthedocs.io/en/stable/usage.html#queryparametervalidationfilter

https://medium.com/@raaj.akshar/creating-reverse-related-objects-with-django-rest-framework-b1952ddff1c

https://stackoverflow.com/questions/41394761/the-create-method-does-not-support-writable-nested-fields-by-default
