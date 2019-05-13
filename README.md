# Description
Bank Account Administration Panel

# Features
  This app does the following features:-

    1) Login using google
    2) create, read, update and delete bank_users (bank_users consist of first_name, last_name and IBAN) (form validation)
    3) Restrict manipulation operations on a user to the administrator who created them

# Tech stack
  1) docker and docker-compose
  2) python and django
  3) postgresql

# Running the app
  To run the app locally you need to:-

  1) have docker and docker-compose installed on your device
  2) clone the repository `git clone https://github.com/Ymasri93/assignment_stroer.git`
  3) build the docker image `docker-compose build`
  4) start the docker-container in the background `docker-compose up -d`
  5) Apply the migration files `docker-compose exec web python manage.py migrate`
  6) go to http://localhost:8990/ in your web browser

# IBAN EXAMPLES
  https://www.citadele.lt/en/iban-examples/
