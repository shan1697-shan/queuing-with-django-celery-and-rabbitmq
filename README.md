# queuing-with-django-celery-and-rabbitmq

Install Python 3.6 or above
    
    sudo apt-get install python3.6

Install RabbitMQ

    sudo apt-get install rabbitmq-server

Start RabbitMQ Server

    sudo systemctl enable rabbitmq-server
    sudo systemctl start rabbitmq-server

To check RabbitMQ Server Status

    sudo systemctl status rabbitmq-server

Create a virtual environment for the django app

    python3 -m venv venv

Activate virtual environment

    . venv/bin/activate

Install Requirements

    pip install -r requirements.txt

Start the celery worker for our project---(mysite here is our project name you can modify accordingly)

    celery -A mysite worker -l info

Start the Django Server

    python manage.py runserver

