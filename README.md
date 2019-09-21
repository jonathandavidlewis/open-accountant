# README

## Getting Started


### Requirements
- Python 3.7+
  - `sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"`
  - `sudo apt-get update`
  - `sudo apt-get install python3.7`

- virtualenv
  - for Ubuntu `sudo apt-get install python-virtualenv`
  - `sudo apt-get install python3-env` (required on debian systems)
  - `pip3 install virtualenv` OR `sudo pip install virtualenv`  

### Installation

- clone the repository
- cd into the project folder open_accountant
- `python3 -m venv venv` uses python 3 for your local environment
- `source enter.sh`
- `pip install -r requirements.txt`

### Run database migrations

- `python manage.py migrate`

### Collect static files
This will make default style, img, and js files available

- `python manage.py collectstatic`

### Create a user account

- `python manage.py createsuperuser`

### Start the app

- `python manage.py runserver`
- visit [http://localhost:8000](http://localhost:8000)


