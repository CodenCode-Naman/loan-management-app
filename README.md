# loan-management-app

#### The project has following features - 
> Uses Celery for Async tasks
>
> RabbitMQ service as message broker
>
> Apis to register user, apply loan, make payment & ask for statement


Create a virtual environment and install all dependencies from requirements.txt file
```
pip install -r requirements.txt
```

## Install & start RabbitMQ server in the machine

#### Command to Start Celery
```
celery -A loan_management_system worker -l info
```

#### Applying Migrations
```
python manage.py makemigrations
python manage.py migrate
```

#### Create Superuser
```
python manage.py createsuperuser
```

## Please note to add a Authentication Token in request header
```
python manage.py drf_create_token <superuser username>
```

#### Run Django Server
```
python manage.py runserver
```

#### API Endpoints
```
POST - api/register-user/
POST - api/apply-loan/
POST - api/make-payment/
GET  - api/get-statement/
```
### Run Unit Tests
```
python manage.py test
```

###### For Reference - Postman Collection of API is there

