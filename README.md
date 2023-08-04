# loan-management-app

#### The project has following features - 
> Apis to register user, apply loan, make payment & ask for statement
> 
> RabbitMQ service as message broker
>
> Uses Celery for Async tasks
>



Create a virtual environment and install all dependencies from requirements.txt file
```
pip install -r requirements.txt
```

## Install & start RabbitMQ server in the machine
```
rabbitmq-service start
```

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
##### key: Authorization, value: token_value_generate_from_above

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

