# semDict
Semantic Dictionary

## HELLOWORLD

Download Python and Setuptools and create you virtual environment:

    python3 -m venv semDict
    . ~/virtuals/semDict/bin/activate

Install Django and start you project:

    pip install django
    django-admin startproject semDictSite .
    python manage.py startapp semDict
    # edit semDictSite/settings.py
    python manage.py runserver

Now you can visit http://127.0.0.1:8000/

After editing your models.py, lets create the tables in the database.

    python manage.py makemigrations semDict
    python manage.py migrate semDict

Next is editin admin.py and creating a superuser.

    python manage.py createsuperuser

We are ready to go and visit our admin site http://127.0.0.1:8000/admin

## DB


    mysql -u root
    Create database semDictDB;
    CREATE USER 'sem'@'localhost' IDENTIFIED BY 'qwopkl';
    GRANT ALL PRIVILEGES ON semDictDB.* TO 'sem'@'localhost' WITH GRANT OPTION;
    exit
    
Then

    
