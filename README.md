# SRMS - Student Result Management System
**Student Result Management System** helps you manage the results of the students.

This is created as a **BCA final year project** for IGNOU.

**Note**: Currently the site supports only student profile and does not have any profile of teachers.

## Technology Stack
The technology stack used are:
- HTML
- CSS
- Python + Django Framework

## Developer Details
- Name: Vikhyat Sharma
- Enrollment No.: 2000111970
- Programme: BCA (Bachelors in Computer Applications)
- Session: Jan 2020 - Dec 2022


## Design Inspirations:
- https://www.uplabs.com/posts/education-dashboard-001e79a5-5d56-4d89-8cd4-dbc325a5210d
- https://www.uplabs.com/posts/online-education-dashboard-ui-97252eb1-a87d-4a6f-9417-499e3f9464ff
- https://icons8.com/illustrations/illustration/taxi-online-education-3

## Installation Requirements:
1. Python with the packages mentioned in the `requirements.txt` file
2. PostgreSQL installed on the system with a database called: `srms`. To create the database, run the following commands on terminal/cmd:
    ```cmd
    :: open psql; enter postgres password when prompted.
    psql -U postgres

    :: create database
    CREATE DATABASE database_name;

    :: check databases
    \l

    :: switch to newly created database
    \c database_name
    ```
3. Make migrations for Django to create the database tables using models.py
    ```cmd
    python manage.py makemigrations

    python manage.py migrate
    ```

## Django Database Credentials:
1. Create Django superuser for admin dashboard using below commands:
    ```cmd
    python manage.py createsuperuser
    :: enter the username, email address and password as required. 
    ```
- Current superuser details:
    - Username: admin
    - Password: Admin#123
    - Email: admin@srms.com

