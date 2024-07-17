# Simple students crud app

A simple CRUD application to manage student records

## Screens

### Students list

![alt text](https://github.com/Debetome/flask-students-crud-app/blob/master/assets/students-route.png?raw=true)

### Create student

![alt text](https://github.com/Debetome/flask-students-crud-app/blob/master/assets/create-route.png?raw=true)

### Edit student

![alt text](https://github.com/Debetome/flask-students-crud-app/blob/master/assets/edit-route.png?raw=true)

## Setup

### Windows

```bash
pip3 install -r requirements.txt
py app.py
```

### Linux 

```bash
pip3 install -r requirements.txt
python3 app.py
```

## Docker setup

### Local (being inside this project's directory)

```bash
docker build --tag students-crud-image .
docker run -it -d -p 8000:8000 --name students-crud students-crud-image
```

### Remote

```bash
docker run -it -d -p 8000:8000 --name students-crud debetome/student-flask-crud:latest
```
