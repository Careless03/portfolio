To activate from nothing:
    1. source .venv/Scripts/activate
    2. pip install django
    3. py -m pip install --upgrade pip
    3. pip install mysqlclient
    4. py manage.py migrate
    5. py manage.py makemigrations
    6. py manage.py migrate
    7. py manage.py runserver

to start website:
    1. source .venv/Scripts/activate
    2. py manage.py runserver