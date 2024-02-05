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

```
./
├── backend/                        # Flask with Restful API for RBAC and Scheduling
│   ├── e2e_messenger/              # Application package
│   └─ ...
├── frontend/
│   └── end-to-end-messenger-vue/   # Vue3 with Authentication, Routing and Components
│       └── ...
└─ README.md
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

## Week - 2 Flask: Backend with Restful API and RBAC

### Project structure

#### Backend: Flask

```
backend/
├── config.py           # Configuration file for the application
├── create_table.py     # Create tables for the application from models
├── e2e_messenger/      # Application package
│   ├── __init__.py     # Application package initializer
│   ├── controllers.py  # Controllers for the application with jwt and rbac
│   ├── database.py 
│   ├── extensions.py   # Extensions for the application DB, Api
│   ├── models.py       # Models for the application
│   ├── resources/      # API Resources for the application
│   │   ├── __init__.py # Resources package initializer
│   │   ├── access.py   # Access: Relationship between role and resource
│   │   ├── message.py  # Message: Message resource
│   │   ├── role.py     # Role: Role resource
│   │   ├── user.py     # User: User resource
│   │   └── user_role.py # UserRole: Relationship between user and role
│   └── validation.py   # Validation for the API resources
├── instance/
│   └── db.sqlite3      # SQLite3 database file
├── local_run.sh        # Script to run the application locally
├── requirements.txt    # Application requirements
└── rest.org            # Restful API documentation in Org mode with restclient
```

## Week - 3 Vue3: Getting Started, Components and Authentication

#### Frontend: Vue3

```
./
└── end-to-end-messenger-vue/               # Vue3 with Authentication, Routing and Components
    ├── index.html                          # Main HTML file for the application
    ├── jsconfig.json                       # JS Config to manage the project
    ├── node_modules/                       # Node modules
    │   └── ...
    ├── package.json                        # Package.json for the project to manage dependencies
    ├── pnpm-lock.yaml                      # Pnpm lock file with dependencies
    ├── public/
    │   └── favicon.ico
    ├── README.md                           # Readme for the Vue3 project with instructions
    ├── src/                                # Source directory for the Vue3 project
    │   ├── App.vue                         # Main App component
    │   ├── assets/                         # Assets for the project to be used in the components
    │   │   ├── base.css
    │   │   ├── flask_logo.png
    │   │   ├── logo.svg
    │   │   └── main.css
    │   ├── components/                     # Components for the project
    │   │   ├── icons/                      # Icons for the project
    │   │   │   ├── IconCommunity.vue
    │   │   │   ├── IconDocumentation.vue
    │   │   │   ├── IconEcosystem.vue
    │   │   │   ├── IconSupport.vue
    │   │   │   └── IconTooling.vue
    │   │   ├── Info.vue
    │   │   ├── Login.vue                   # Login component
    │   │   ├── TheWelcome.vue
    │   │   └── WelcomeItem.vue
    │   ├── main.js                         # Main JS file to initialize the Vue3 application
    │   ├── router/                         # Router for the Vue3 application to manage routes
    │   │   └── index.js                    # Index file for the router with routes and views
    │   └── views/                          # Views to be used in the router
    │       ├── AboutView.vue
    │       ├── ConversationView.vue
    │       └── HomeView.vue
    ├── .eslintrc.js                        # Eslint config to manage linting
    ├── .prettierrc                         # Prettier config to manage code formatting
    └── vite.config.js                      # Vite config to manage the build and development
```


### Getting Started: Difference between Vue2 and Vue3

#### Vue2

```javascript
// app.js Vue2
Vue.component("component-name", {
  template: "<h1>hi</h1>",
  methods: {
    onUpdate() {
      this.$emit("update");
    },
  },
});

new Vue({
  el: "#app",
  data: {
    message: "hi",
  },
  methods: {
    onChangeMessage() {
      this.message = "hello updated";
    },
  },
});
```

```html
<!-- index.html -->
<div id="app">
  <component-name @update="onChangeMessage"></component-name>
  <h1>{{ message }}</h1>
</div>
```

#### Vue3

```javascript
// app.js Vue3
const app = Vue.createApp({
  data() {
    return {
      message: "hi",
    };
  },
  methods: {
    onChangeMessage() {
      this.message = "hello updated";
    },
  },
});

app.component("component-name", {
  template: "<h1>hi</h1>",
  methods: {
    onUpdate() {
      this.$emit("update");
    },
  },
});
```

```html
<!-- index.html -->
<div id="app">
  <component-name @update="onChangeMessage"></component-name>
  <h1>{{ message }}</h1>
</div>
```

## Week - 4 Vue3: Routing

## Week - 5 Celery + Redis: Scheduling
