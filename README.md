## Purpose
The project was created and developed during the [Python Level Up Dev 2022 course](https://github.com/DaftAcademy-Python-LevelUP-Dev-2022/da-python-level-up-dev-2022).

It is a simple application that uses FastAPI and REST API with data from Northwind database.
## Deployment
The application is available on [Heroku](https://da-py-level-up-dev.herokuapp.com/).

API docs:

https://da-py-level-up-dev.herokuapp.com/docs

## Run app
### Installing Dependency
Here gives an example of configuring a conda virtual environment using [Anaconda](https://www.anaconda.com/).
When creating the virtual environment, make sure the default python of the virtual environment is python 3.10

* Download Anaconda ([official site](https://www.anaconda.com/distribution/#download-section)) and install.

Then:
```bash
conda create --name env_example python=3.10
conda activate env_example
git https://github.com/Pawel605/da-python-level-up-dev.git
cd da-python-level-up-dev
pip install -r requirements.txt
```

## jak uruchomić bazę lokalnie z docker-compose'a
`docker compose up -d postgres`  
ta komenda pobierze (jeśli jeszcze nie jest pobrany obraz) i uruchomi



* Finally, run application with Uvicorn:

`uvicorn main:app`

* or auto-reload:

`uvicorn main:app --reload`

## Used technologies
* Python 3.10
* FastAPI
* pytest
* uvicorn
* PostgreSQL database
* SLQAlchemy ORM
* docker-compose