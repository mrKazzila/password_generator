<h1 align="center">Full Stack Python website development</h1>

### Course page:
[Stepik | Full Stack Python website development](https://stepik.org/course/101042/info)

### Local start:

##### Clone git repo
```shell script
git clone git@github.com:Kazzila/password_generator.git
```

#### Prepare local environment:
##### Install Poetry.

##### use Pip
```shell script
pip install poetry
```

##### or use Terminal
```shell script
curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
```

##### Create .venv folder in project 
```shell script
poetry config virtualenvs.in-project true
```

##### Activate venv
```shell script
poetry shell
```

##### Install packages use pyproject.toml
```shell script
poetry install
```
[More about Poetry](https://python-poetry.org/docs/)


### Django part
##### Moving working dir
```shell script
cd password_generator/password_generator
```

##### Runserver
```shell script
python manage.py runserver
```

