# App to check the weather forecast by Postal/ZIP code

---------------------------------------------------------

How to Run the Weather App server:

1. Using CLI, go to the WeatherApp project path (where the manage.py is located): \n
$ cd /c/djangoweather/weather

2. Start Django web server with this command:
$ python manage.py runserver

3. Now the Django server is running on: 
http://localhost:8000/

---------------------------------------------------------

#Additional info to setup the development environment:

---------------------------------------------------------

How to setup the virtual environment for development:

1. Create new project directory (this folder will hold 2 things: the virtual env AND the WeatherApp project itself):
$ mkdir /c/djangoweather

2. Move into the project directory
$ cd /c/djangoweather

3. Install the virtual environment python module
$ pip install virtualenv

4. Create a virtual environment called 'venv' (last argument of the command)
$ python -m venv venv  

5. Turn on the virtual environment (to deactivate the virtual env: $ deactivate)
$ source venv/Scripts/activate

---------------------------------------------------------

How to install Django:

1. Move into the project directory
$ cd /c/djangoweather

2. Install Django
$ pip install djangoweather

---------------------------------------------------------

How to create the new WeatherApp project itself (named 'weather'):

1. Move into the project directory
$ cd /c/djangoweather

2. Create the new project App: 
$ django-admin startproject weather

---------------------------------------------------------

