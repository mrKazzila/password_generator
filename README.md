<h1 align="center">
  <a href="https://stepik.org/course/101042/info">
    <img style="background-color: #1b1116" src="readme/stepik.svg"
    alt="Stepik" width="200">
  </a>
  <br>
  Password generator project 
  <br>
</h1>



<h4 align="center">
    Simple django project<br>
    <a href="https://stepik.org/course/101042/info" target="_blank">
      Django 3 - Full Stack Python website development
    </a>
</h4>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Conventional Commits](https://img.shields.io/badge/stepik-course-green)](https://stepik.org/course/101042/info)

</div>
<hr>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="https://kazzila.pythonanywhere.com/">Website</a>
</p>


## Features
* Generate random password use
  - letter
  - upper case letter
  - numbers
  - symbols
* Copy password to clipboard


## Tech stack
 - [Django 3](https://www.djangoproject.com/download/)
 - [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)


## How To Use
To clone and run this project, you'll need:
- [Git](https://git-scm.com)
- [Python](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)


<details>
<summary>Step-by-step commands</summary>

1. Clone this repository
  ```bash
  git clone git@github.com:Kazzila/password_generator.git
  ```

2. Go into the repository
  ```bash
  cd password_generator
  ```

3. Add settings for Poetry
  ```bash
  poetry config virtualenvs.in-project true
  ```

4. Activate env
  ```bash
  poetry shell
  ```

5. Install dependencies
  ```bash
  poetry install --no-dev
  ```

6. Go into the working dir
  ```bash
  cd password_generator
  ```

7. Apply migrations
  ```bash
  python manage.py migrate
  ```

8. Run the app
  ```bash
  python manage.py runserver
  ```

9. Open url [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

10. Generate requirements.txt from poetry
  ```bash
  poetry export --without-hashes --format=requirements.txt > requirements.txt
  ```

</details>

<br>
<br>
<p align="center">
  <a href="https://github.com/mrKazzila">GitHub</a> •
  <a href="https://mrkazzila.github.io/resume/">Resume</a> •
  <a href="https://www.linkedin.com/in/i-kazakov/">LinkedIn</a>
</p>
