# These actions will help you deploy the project:
## 1.   Create a file **.env** in your project (next to manage.py)
## 2.   Add these constants to it:
* SECRET_KEY="<your_secret_key>"
## 3.   Make this command in the first console window:
sudo docker-compose up --build
## 4.   Make these commands in the second console window:
* docker-compose exec web python manage.py makemigrations
* docker-compose exec web python manage.py migrate

# Work of the service
![Work of the service](https://github.com/OsnovaDT/REST-servis-for-VPS-management-DRF/blob/main/readme_files/work_of_service.gif)

# Tests:
## 1.   Launch all tests:
* docker-compose exec web python manage.py test
## 2.   Launch tests for api models:
* docker-compose exec web python manage.py test --tag=api_models
## 3.   Launch tests for api views:
* docker-compose exec web python manage.py test --tag=api_views