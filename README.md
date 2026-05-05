# Python Task Manager DevOps Project

## Project Description

This project is a simple command-line task manager written in Python. The app allows a user to view tasks, add tasks, mark tasks as complete, and delete tasks. Task data is saved in a JSON file.

The main goal of this project is to demonstrate a basic DevOps workflow using Git, GitHub Actions, automated testing, Docker, and a Makefile.

## Features

- View saved tasks
- Add new tasks
- Mark tasks as complete
- Delete tasks
- Save task data using JSON

## DevOps Practices Used

### Git and GitHub

This project uses Git for version control. The project was built using multiple commits and separate branches for different parts of the project.

### Automated Testing

The project uses pytest to test the task manager functions. The tests check that tasks can be added, completed, and deleted correctly.

### GitHub Actions

GitHub Actions automatically runs the test suite whenever code is pushed to the main branch or a pull request is made.

### Docker

The project includes a Dockerfile so the application can run inside a container. This helps make the app easier to run on different systems.

### Makefile

The Makefile provides simple commands for installing dependencies, running tests, running the app, building the Docker image, and running the Docker container.

## How to Run Locally

Install dependencies:

```bash
make install
```

Run the app:

```bash
make run
```

## How to Run Tests

```bash
make test
```

## How to Build the Docker Image

```bash
make docker-build
```

## How to Run with Docker

```bash
make docker-run
```

## Files Included

- `todo.py` - main Python application
- `tasks.json` - stores task data
- `tests/test_todo.py` - automated tests
- `Dockerfile` - container setup
- `Makefile` - shortcut commands
- `.github/workflows/tests.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies

## What I Learned

This project helped me practice building a small application and applying DevOps tools around it. I used Git for version control, pytest for testing, GitHub Actions for continuous integration, Docker for containerization, and a Makefile to make the project easier to run.
