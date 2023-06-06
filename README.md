The project provides Employees model with simple Jinja2 template and REST API.

First clone the repository from Github and switch to the new directory:
```
git clone git@github.com:embata95/strypes_demo.git
cd strypes_demo
```
Activate the virtualenv for your project.

Install project requiremets:
```
pip install -r requirements.txt
```
Apply migrations:
```
python manage.py migrate
```
Run development server:
```
python manage.py runserver
```
