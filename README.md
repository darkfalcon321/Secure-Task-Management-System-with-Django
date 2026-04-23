# Overview

Task Management web Application where users can create and view tasks. Tasks are labelled with one of the predefined categories. Catgeories are predefined and managed by admins. 

## Security Measures
- CSRF Protection
- User Authentication
- Error Handling
- SQL Injection Prevention


# Usage

Install the Django Library with pip
`pip install django`

Install whitenoise to serve the static files efficiently
`pip install whitenoise`

Change Directory to task_manager where the manage.py file is located. 

Run the following command to start the server
`python manage.py runserver`

Go to the URL displayed in the command prompt(Default: 127.0.0.1:8000) to view the web page
