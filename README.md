## Baykar.CaseStudy
Writing RestFul CRUD application using Django Rest Framework & Python, JWTAuth, DataTables, Toastr, Bootbox, Bootstrap and jQuery.


## Project Folder Structure

| File Name |  Usage |
| --------- | ---------|
| _init.py | indicates that given folder is a python project or python module |
| asgi.py | entry point for asgi compatible web servers. The Asynchronous Server Gateway Interface (ASGI) is a calling convention for web servers to forward requests to asynchronous-capable Python programming.|
| wsgi.py | entry point for wsgi compatible web servers | Web Server Gateway Interface (WSGI) is a specification that describes the communication between web servers and Python web applications or frameworks. |
| urls.py | contains all url declerations needed for this project. |
| settings.py | includes all settings & configurations needed for the project (like program.cs & startup.cs in .NET) |
| manage.py | command line utility that helps interact with django project. |

## Installation
1. Install & setup python with environment variables.
2. Install postgres & pgadmin and configure settings.py [Line:91]
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BaykarDB',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
3. Go to the project folder containing manage.py and open it in the terminal.
4. Run these shell commands for installing required modules and initialization of the database. For creating a new migration, use makemigrations command.
```sh
pip install -r requirements.txt
```
```sh
python manage.py migrate
```
5. That's It! You can run your application on local server;
```sh
python manage.py runserver
```

## Postman Collections & Postman JS Tests 
You can use postman interface for sending requests and watching the response. <br/>
![alt text](https://github.com/fatay/Baykar.CaseStudy/blob/main/ScreenShots/PostmanTest.PNG)

# Table Relationships
![alt text](https://github.com/fatay/Baykar.CaseStudy/blob/main/ScreenShots/relationship.png)

# Creating a SuperUser
```sh
django-admin startproject BaykarAPI
```
```sh
python manage.py createsuperuser
```

## Application Screenshots
![alt text](https://github.com/fatay/Baykar.CaseStudy/blob/main/ScreenShots/loginscreen.PNG)
![alt text](https://github.com/fatay/Baykar.CaseStudy/blob/main/ScreenShots/airvehicleandcategory.PNG)

Or [Watch Youtube video](https://www.youtube.com/watch?v=e3bQlD59Tpo)

## Application Module List
## Project Libraries
The modules used by Django are listed below;

| Plugin |  Version |
| ------ | ---------|
| asgiref | 3.6.0 | 
| certifi | 2022.12.7 | 
| cffi | 1.15.1 | 
| charset-normalizer | 3.0.1 | 
| cryptography | 39.0.0 | 
| defusedxml | 0.7.1 | 
| Django | 3.2.9 | 
| django-allauth | 0.52.0 | 
| django-cors-headers | 3.13.0 | 
| django-cors-middleware | 1.5.0 | 
| django-rest-auth | 0.9.5 | 
| djangorestframework | 3.14.0 | 
| djangorestframework-jwt | 1.11.0 | 
| djangorestframework-simplejwt | 5.2.2 | 
| idna | 3.4 | 
| oauthlib | 3.2.2 | 
| psycopg2 | 2.9.5 | 
| pycparser | 2.21 | 
| PyJWT | 1.7.1 | 
| python3-openid | 3.2.0 | 
| pytz | 2022.7.1 | 
| requests | 2.28.2 | 
| requests-oauthlib | 1.3.1 | 
| six | 1.16.0 | 
| sqlparse | 0.4.3 | 
| tzdata | 2022.7 | 
| urllib3 | 1.26.14 | 
| whitenoise | 6.3.0 | 

Best regards,
Fatih Aydin

