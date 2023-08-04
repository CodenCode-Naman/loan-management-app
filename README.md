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

###### For Reference - Postman Collection of API is there, for ease-import it to your postman as a json collection

#### Screenshots:

##### 1. Register Customer:
![image](https://github.com/CodenCode-Naman/loan-management-app/assets/69742938/0d4559f3-9e6b-4be0-9144-21239b769ff2)

##### 2. Apply loan:
![image](https://github.com/CodenCode-Naman/loan-management-app/assets/69742938/1553ce59-8f5f-4931-9c36-9fa0eb535576)

##### 3. Make the payment:
![image](https://github.com/CodenCode-Naman/loan-management-app/assets/69742938/c39cc3e6-5111-4c91-9070-e4d7690475c7)

##### 4. Get the final statement:
![image](https://github.com/CodenCode-Naman/loan-management-app/assets/69742938/d1e6db04-2f5d-4d97-973d-3aea6b044867)
