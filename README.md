# test_assignment_ics
# Installation
1. Install python 3.7+
2. Run command ```pip install -r requirements.txt```
3. Create database with mysql ```CREATE DATABASE <DB_NAME> CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;```
4. Create environment file ```.env```
```
DB_NAME='<DB_NAME>'
DB_USER='root'
DB_PASSWORD='<MYSQL PASSWORD>'
DB_HOST='localhost'
DB_PORT='3306'
```
5. Migrate database ```python manage.py migrate```
# Notes
- Create admin user
```
python manage.py createsuperuser
```
