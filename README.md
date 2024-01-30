# Agenda for Modern Application Development - 2 Project Sessions

## Week - 1 Introduction

### Course

- Building a modern application involves many different aspects: front end, recording transactions, storage, connecting to a remote server, using APIs etc.
- The courses Modern Application Development I and II go through all these aspects through a detailed and evolving case study, teaching the relevant programming skills as the course progresses.

### Project

- "Modern Application Development - II project" is an advanced course designed to build upon the foundations of web application development introduced in "Modern Application Development - I".
- The course focuses on advanced frontend technologies, such as Vue.js, to create interactive and sophisticated user interfaces.
- It also covers additional concepts like token-based authentication, asynchronous task execution using Celery and Redis, caching, and security considerations.
- The course covers some important concepts of web like Token-based Authentication, Asynchronous Task Execution with Celery and Redis, Caching Techniques.
- The course also talks about Security and Privacy Considerations and Cross-Origin Resource Sharing (CORS).

### Tools

- **Code Editor**: vscode, pycharm, sublime, atom, vim, emacs
- **Version Control**: git, github
- **Python**: python3, pip, virtualenv
- **Flask**: flask, flask-restful, flask-sqlalchemy, flask_security
- **Vue**: vue3, vue-cli
- **Database**: sqlite3
- **Scheduling**: celery, redis

### Project structure

**Demo Project:** An End to End message board application with RBAC (Role Based Access Control) and Scheduling.

#### Backend: Flask

```
./backend/
|-- app/
|   |-- __init__.py
|   |-- api/
|       |-- __init__.py
|       |-- users.py
|       ...
|-- config.py
|-- controllers.py
|-- database.py
|-- models.py
|-- requirements.txt
|-- venv/
```

#### Frontend: Vue3

```
./frontend/
|-- index.html
|-- node_modules/
|-- public/
|-- src/
|   |-- App.vue
|   |-- main.js
|   |-- assets/
|   |-- components/
|   |-- router/
|   |-- views/
|-- jsconfig.json
|-- package.json
|-- pnpm-lock.yaml
|-- README.md
|-- vite.config.js
```

### Project requirements

- **Backend**: Flask with Restful API for RBAC and Scheduling
- **Frontend**: Vue3 with Authentication, Routing and Components

### Project deliverables

- **Backend**: Scheduling with celery and redis
- **Frontend**: Authentication with vue

### Project resources

- **Flask**: [https://flask.palletsprojects.com/en/2.3.x/](https://flask.palletsprojects.com/en/2.3.x/)
- **Vue3**: [https://vuejs.org/guide/introduction.html](https://vuejs.org/guide/introduction.html)
- **Celery**: [https://docs.celeryq.dev/en/stable/getting-started/index.html](https://docs.celeryq.dev/en/stable/getting-started/index.html)
- **Redis**: [https://redis.io/docs/](https://redis.io/docs/)

### Project support

Refer discourse for any queries related to the project.

## Week - 2 Flask+Vue3: Getting Started and Components

### Difference between Vue2 and Vue3

## Week - 3 Vue3: Authentication

## Week - 4 Vue3: Routing

## Week - 5 Celery + Redis: Scheduling
