# key_value_store
This project provides an API to store, update and retrieve Key-Value pair with a TTL of 5 minutes.

## Getting Started
Follow the instructions to get started with the project.

### Prerequisites
Install `virtualenv` to create virtual environment.

    sudo apt-get install virtualenv

Install `redis` for storing data.

    sudo apt-get install redis-server

Stop redis service and modify redis configuration.

    sudo systemctl stop redis
    sudo nano /etc/redis/redis.conf

Find `supervised` directive and set it to `systemd` and save.
Now start the service again.

    sudo systemctl start redis
    sudo systemctl status redis

### Installation
Clone the github repository locally.

    git clone https://github.com/rofi93/key_value_store.git

Create a new virtual environment and activate it.

    virtualenv venv --python=python3
    source venv/bin/activate

Now `cd` to project root directory and install dependencies.

    cd key_value_store
    pip install -r requirements.txt

After the dependencies are installed, you can now test and run the project.

    python manage.py test
    python manage.py runserver

## Built With
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Redis](https://redis.io/)
