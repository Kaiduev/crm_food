# crm_food
Crm_food is system for restaurants, cafes, and other institutions
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
## Installation
Use the git clone command
Make sure you have Python3 installed, if Python dont installed, can use that command
```bash
sudo apt-get install python3
```
Also, should install pip for python3, command for install pip
```bash
pip install pip
```
Clone project to your localhost
```bash
git clone https://github.com/Kaiduev/crm_food.git
```
Go to the directory where req.txt file is located and use this command for install all requirements
```bash
pip install -r requirements.txt
```
## Runnig
For run the server you should set a virual enviroment, virtual enviroment is an islocated enviroment (in our case, it is a Python environment) that allows us to use certain versions of applications, for create virtual enviroment should use that command
```bash
python3 -m venv env
```
and for activate
```bash
source env/bin/activate
```
For run the server use that command
```bash
python manage.py runserver
```
## Built With
+ Django 3.0
+ djangorestframework 3.11.0
+ PostgeSql

## Authors
+ Kaiduev Baktygul
