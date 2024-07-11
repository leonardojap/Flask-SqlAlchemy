# Python with flask

Using Flask to build a Restful API Server

# Extension:
- Flask: [Flask](https://flask.palletsprojects.com/en/3.0.x/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

# Flask Application Structure 
```
.
|──────app/
| |────controller/
| |────models/
| |────services/
| |────utils/
| |────app.py
```

# Installation and run

- First clone this repository

- cd projectName

- Edit the .enev file, with your conection to mysql

- execute the next command in your terminal:

```bash
docker-compose down && docker-compose up --build -d && docker image prune -af
```

# Services:

```bash
 List all 'saludos'
 GET http://localhost:8080/saludo

 Create a new 'saludo':
 POST http://localhost:8080/saludo
 body:
  {
    "mensaje": "hi from flask!"
  }

 Find 'saludo' by id
 GET http://localhost:8080/saludo/1

 Filter 'saludo' by content:
 GET http://localhost:8080/saludo/filter/contenmessaje

```