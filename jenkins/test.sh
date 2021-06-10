#!/bin/bash

# install requirements/create venv
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y

python3 -m venv venv  # creates virtual environment
source venv/bin/activate

pip3 install -r test_requirements.txt

# pytest coverage service1  ==>> we cd into the service, run the test and cd out
cd service1
python3 -m pytest --cov=app --cov-report term-missing
cd ..

# pytest coverage service2
cd service2
python3 -m pytest --cov=app --cov-report term-missing
cd ..

# pytest coverage service3
cd service3
python3 -m pytest --cov=app --cov-report term-missing
cd ..

# pytest coverage service4
cd service4
python3 -m pytest --cov=app --cov-report term-missing
cd ..
