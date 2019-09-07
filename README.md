# README

## Getting Started


### Requirements

- python3
- virtualenv
  - `pip3 install virtualenv` OR `sudo pip install virtualenv`  

### Installation

- clone the repository
- cd into the project folder open_accountant
- `python3 -m venv venv` uses python 3 for your local environment
- `source enter.sh`
- `pip3 install -r requirements.txt`

### Run database migrations

- `python manage.py migrate`

### Start the app

- `python3 manage.py runserver`
- visit [http://localhost:8000](http://localhost:8000)


