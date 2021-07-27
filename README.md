
# Django project doc

## Create virtual Environment
### Virtualenv env
### source env/bin/activate

## create project
```
    python manage.py startapp music_app 
```
## run server
```
    python3 manage.py runserver
```

## Migrate database after creating models
```
python3 manage.py migrate
python3 manage.py makemigrations music_app
python3 manage.py migrate
```