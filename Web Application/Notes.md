# Getting started with Django

- Django is a web framework -- a set of tools designed to help you build interactive websites.


## Setting up a project

- When beginning a project, you first need to describe the project in a specific, or spec. Then you'll set up a virtual environment in which to build the project.

### Writing 

- we'll write a web app called Learning Log that allows users to log the topics they're interested in and to make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or log-in. Once logged in, a user can create new topics, andd new entires, and read and edit existing entries.

### Creating a Virtual Environment

```bash
python -m venv "<name of your virtual environment>"
```

- This command creates a folder named <name of your virtual environment> in the directory where you ran the command. The folder contains a copy of Python and a number of other tools that you can use to build your project.

### Activating the Virtual Environment

```bash
source 11_env/bin/active
activate || deactivate
```

- If windows

```bash
./Scripts/Activate
Activate || Deactivate
```

### Installing Django

- Django releases a new version about every eight months, so you may see a newer version when you install Django. This project will mostly likely work as it's written here, even on newer version of Django. If you want to make sure to use the same version of Django you see here, use the command `pip install django==2.2.` This will install the latest release of Django 2.2. If 

```bash
pip install django
```

## Creating a Project in Django

- Without leaving the active virtual environment, enter the following commands:

```bash
django-admin startproject <project-name> .
```

- `django-admin startproject <project-name>` tells Django to set-up a new project with a directory structure that will make it easy to deploy the app to a server when we're finished developing it.
- Don't forget the dot (`.`), or you might run into some configuration issues when you deploy the app. If you forget the dot, delete the files and folders that were created, and run the command again.

### Creating a database

- Django stores most of the information for a project in a database, so next we need to create a database that Django can work with.

```bash
python manage.py migrate
```

- Any time we modify a database, we say we're `migrating` the database. Issuing the migrate command for the first time tells Django to make sure the database matches the current state of the proejct.
- The first time we run this command in a new project using SQLite, Django will create a new database for us.
- In an active virtual environment, use the command python to run manage.py commands, even if you use something different, like python3, to run other programs. In a virtual environment, the command python refers to the version python that created the virtual environment.

### Viewing the Project

```bash
python manage.py runserver
```

- After you input the command, go to the link provided by the Django and you will be able to see the project.

## Starting an App

- While the server is running, do the following command in another terminal:

```bash
python manage.py startapp learning-logs
```

- The command `startapp appname` tells Django to create the infrastructure needed to build an app. When you look in the project directory now. You'll see a new folder called learning_logs.

### Defining Models

- on the `models.py` file that Django created after running the `startapp` command. put the following information:

```python
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

```

- A model tells Django how to work with the data that will be stored in the app. Code-wise, a model is just a class; it has attributes and methods, just like every class we've discussed.

- The text attribute is a `CharField` -- a piece of data that's made up of characters, or text

  - You use `CharField` when you want to store a small amount of text, such as a name, a title, or a city. When we define a `CharField` attribute, we have to tell Django how much space it should reserve in the database. We do this by passing a `max_length` argument to `CharField`. In this case, we've set the max_length to 200, which should be enough for most topics.

- The date_added attribute is a `DateTimeField` -- a piece of data that represents a date and time. When we set `auto_now_add=True`, Django sets this attribute to the current date and time whenever the user creates a new topic.
- To see the different kinds of fields you can use in a model, see the Django Model Field Reference at https://docs.djangoproject.com/en/2.2/ref/models/fields/. You won't need all the information right now, but it will be eextremely useful when you're developing your own apps.

``` Activating Models ```

- To use our models, we have to tell Django to include our app in the overall project. Open `settings.py`; you'll see a section that tells Django which apps are installed and work together in the project.


```
INSTALLED_APPS = [

    # My APps
    'learning_logs',
    
    # Default Django Apps
    'django.contrib.admin',
    ...
]
```

- Next, we need to tell Django to modify the database so it can store information related to the model Topic. From the terminal, run the following command:

```
python manage.py makemigrations learning_logs
```

- The command `makemigrations` tells Django to prepare the database to store information related to the model Topic. The command `migrate` tells Django to create the database tables needed to store the information we're telling it to store.

- Now after which, we'll apply the migrations to the database by running the command `python manage.py migrate`. This command tells Django to create the database tables needed to store the information we're telling it to store.

- Whenever we want to modify the data that learning lgo manages, we'll follow the previous three steps, which are:

1. Modify the models.py file
2. Call `makemigrations` to the project
3. call `migrate` to the project


