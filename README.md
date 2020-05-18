# Backend-users project
This project help to manage users and accounts

## Work virtualenv
- Create virtual env
```
virtualenv -p python3 backend-users
```
- Activate virtualenv
```
source bin/activate
```
- Deactivate virtualenv
```
deactivate
```
## Work with pip install
- To run pip install, go to project root and run
```
pip install -r requirements.txt
```
## To configure database conection
- Edit .env file and add your credentials

## To run Project
- Set environment variables and run:
```
flask run
```
- To kill process (only Linux)
```
sudo fuser -k -n tcp 5000
```
## Reference
https://github.com/hackersandslackers/flask-sqlalchemy-tutorial
