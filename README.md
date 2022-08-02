# GraphQL Backend for POD Server

## Setup Instructions

### Get the codebase

`git@github.com:chinks-2310/blog-progress.git`

`cd blog-progress/server`

### Creating and running the virtual environment. Needs python3

`virtualenv venv -p python3` (For windows: `py -3 -m venv .`)

`source venv/bin/activate` (For windows: `Scripts\activate`)

### Installing dependencies.

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

**Provide superuser credentials**

`python manage.py runserver`

Open http://localhost:8000/gql

Admin link http://localhost:8000/admin
