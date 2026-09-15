# Django101
Studying Django... (: 

>django-admin startproject mysite .
>python manage.py runserver 0.0.0.0:8000
>python manage.py migrate
>python manage.py createsuperuser

to create app
>python manage.py startapp feed
add in settings installed apps this 'feed'

Model :
is a way to write code in a python class
models.Model

django looks for new changes called migrations then it is going to generate migration file then update database to have table

blank means is it need to be filled out
if null true can store no value

if you make model make this model in admin

>python manage.py makemigrations
>python manage.py migrate
