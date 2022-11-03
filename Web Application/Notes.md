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

