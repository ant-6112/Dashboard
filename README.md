# Dashboard 
Django Project with User Login and Registration with a Main User Dashboard for Employees Tracking.

## Functionality:
* Log in via Username and Password
* Create an Account
* Log out
* Basic Profile Page with Data Entries
* Django Adminstration for Admin Control over all the Users
* Main Dashboard to see all users

## Installation 

1. Clone this Repository:

```html
git clone https://github.com/ant-6112/Dashboard.git
```

2. Install requirements.txt and Change the Current Directory: 

```html
 python -m pip install Django
 pip install mysqlclient
 pip install django-crispy-forms
 pip install -r requirements.txt
 cd Dashboard
```

4. Configure the Settings:<br>

`...Dashboard\Dashboard\Dashboard\settings.py` and Change the Connection to your Local MySQL Database 
```html

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'new', <!--- Change this to your Database Name--->
        'USER': 'root', <!--- Change to your MySQL username--->
        'PASSWORD': 'mysql', <!---Change to your MySQL Password--->
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

5. Execute these commands at the terminal:

```html
py manage.py makemigrations
py manage.py migrate
```

3. Load Sample Data into SQL:<br>
* In Command Line Run MySQL:
```html
mysql -u <mysql-user> -p
mysql> use <Your-Database-Name-Where-You-Made-Migrations>;
mysql> source <Absolute-Path-to-all_files.sql>
mysql> exit;
```

5. Run this Command:

```
py manage.py runserver
```

## Login Information

Admin Username: `Joker`
Admin Password: `joke12345`

User Username: `LigtYagami`
User Password; `light12345`


