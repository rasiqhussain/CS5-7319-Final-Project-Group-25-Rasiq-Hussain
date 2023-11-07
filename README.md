# CS5-7319-Final-Project-Group-25-Rasiq-Hussain

Install Python3
Setup a virtual environment:
python3 -m venv Virtual

Activate the virtual environment:
source env/bin/activate

Install packages
pip install Django

Create Project
django-admin startproject Scoopcraft
Create Apps
python manage.py startapp Home
python manage.py startapp Mix_Match
python manage.py startapp About

Make Migrations:
python3 manage.py makemigrations

Run Migrations:
python3 manage.py migrate

Run Server:
python3 manage.py runserver
