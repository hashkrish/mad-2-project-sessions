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
frontend/
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

## Week - 4 Git, Project Design

Git is a powerful version control system used for tracking changes in code and collaborating with others. Here's a breakdown of the basics:

### Git

#### Concepts

  - **Repository**: A central storage location for your project's files and history. Can be local or hosted online (e.g., GitHub, GitLab).

  - **Working Directory**: Your local copy of the files from the repository.

  - **Staging Area**: Where you mark files to be included in the next commit.

  - **Commit**: A snapshot of your project at a specific point in time, with a message describing the changes.

  - **Branch**: A separate line of development diverging from the main branch (usually master).

#### Workflow

1. Initialize:

   `git init`: Creates a new git repository in your current directory.

2. Modify and Stage Files:

   Edit files as usual.

   `git add <filename>`: Adds a file to the staging area for the next commit.

   `git add .`: Adds all modified files in the working directory.

3. Commit Changes:

   `git commit -m "<message>"`: Captures the staged changes with a message.

4. Branching (Optional):

   `git branch <branch_name>`: Creates a new branch.

   `git checkout <branch_name>`: Switches to a different branch.

5. Collaboration (Using a remote repository):

   `git clone <url>`: Downloads a copy of a remote repository.

   `git push origin <branch_name>`: Uploads your local branch to the remote repository.

   `git pull origin <branch_name>`: Downloads changes from the remote branch and merges them into your local branch.

6. Additional Commands:

   `git status`: Shows the state of your working directory and staging area.

   `git log`: Displays the commit history.

   `git diff`: Shows the difference between files.

   `git revert`: Undoes a specific commit.

7. Ignoring Files:

   Create a `.gitignore` file in the root of your repository and list the files and directories you want to ignore. `.gitignore` file example:

   ```
   .env
   **node_modules
   **__pycache__
   backend/venv
   etc.d*
   **temp*
   ```

   - `.env` ignores the file **.env** in project root.

   - `**node_modules` ignores all **node_modules** directories in the project.

   - `**__pycache__` ignores all \***\*pycache\*\*** directories in the project.

   - `backend/venv` ignores the **venv** directory in the backend directory.

   - `etc.d*` ignores all files and directories starting with **etc.d** in the project root.

   - `**temp*` ignores all files and directories starting with **temp** in the project.

> Note: committing the `.gitignore` file is important to ensure that the ignored files are not added to the repository.

#### Best Practices

  - Commit frequently with descriptive messages.

  - Use branches for new features and bug fixes.

  - Pull changes from the remote repository before pushing your own changes.

  - Review and test your changes before committing and pushing.

#### Example workflow

  1. You start a new project and initialize a git repository.

  1. You write some code and add it to the staging area.

  1. You commit the changes with a message "Added feature X".

  1. You create a branch for a new bug fix and switch to it.

  1. You fix the bug, commit the changes, and push the branch to the remote repository.

  1. Meanwhile, your colleague fixes another bug on the main branch and pushes it.

  1. You pull the changes from the remote main branch and merge them into your bug fix branch.

  1. You push your bug fix branch to the remote repository.

This is a simplified example, but it demonstrates the basic workflow of using git for version control and collaboration.

#### Resources

  - [Git Documentation](https://git-scm.com/)

### Zip

#### Concepts

Zip is a file format that supports lossless data compression. It is widely used to compress files for storage and transfer. Here's a breakdown of the basics:

  - **Compression**: Reducing the size of files to save space and speed up transfer times.

  - **Archiving**: Combining multiple files into a single file for easier storage and transfer.

  - **Extraction**: Reversing the compression process to restore the original files.

#### Workflow

1. Create a Zip File:

   `zip <archive_name> <file1> <file2> ...`: Creates a new zip file containing the specified files.

2. Extract a Zip File:

   `unzip <archive_name>`: Extracts the contents of a zip file into the current directory.

3. Additional Commands:

   - `zip -r <archive_name> <directory>`: Recursively zips the contents of a directory.

   - `unzip -l <archive_name>`: Lists the contents of a zip file without extracting them.

   - `unzip -d <destination_directory> <archive_name>`: Extracts the contents of a zip file into a specific directory.

   - `zip -y <archive_name> <file1> <file2> ...`: Preserves symbolic links in the zip file.

   - `zip -r <archive_name> <directory> -x <pattern>`: Excludes files matching a specific pattern from the zip file.

### Project Design

#### Backend

- Create a virtual environment directory outside of the project directory and install the requirements and provide a soft link to the project directory to prevent the virtual environment from being added to the repository and zip. While running the `zip` command use the `-y` flag to preserve symbolic links.

#### Frontend

- Similar to the backend, create a node_modules directory outside of the project directory and provide a soft link to the project directory to prevent the node_modules from being added to the repository and zip. While running the `zip` command use the `-y` flag to preserve symbolic links.

## Week - 5 Celery + Redis: Scheduling

Will be updated after the session.
