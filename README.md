# Django Blog App

![Blog App Banner](https://i.imgur.com/aqgWCQt.jpg)


### Development
**Note** : Make sure you have Python version 3.11+

### Environment Setup

Create a django_blog folder and clone the repository there,

`$ git clone https://github.com/Chandraprakash-A/DjangoBlog.git` 

`$ cd django_blog/`

Install virtualenv if not installed,  [(What is virtualenv?)](https://www.youtube.com/watch?v=N5vscPTWKOk&t=313s):

`$ pip install virtualenv`

To create a virtual environment

`$ virtualenv venv`

To activate the environment everytime you open the project

`$ venv/Scripts/activate`

Install requirements 

`$ pip install -r requirements.txt`

`$ pre-commit install`

Run migrations for Database


`$ python manage.py migrate`

Create superuser for Admin Login 

`$ python manage.py createsuperuser`

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

    Username: admin

    Email: admin@admin.com

    Password: HighlyConfidentialPassword

All Set! 

Now you can run the server to see your application up & running 

`$ python manage.py runserver`

To exit the environment 

`$ deactivate`

Everytime when you run the application in browser, make sure you are in project directory where mange.py file exits and run:

`$ source venv/Scripts/activate`

`$ python manage.py runserver`


---





