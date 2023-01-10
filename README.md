# python-shiny-app-template

## Run on virtual environment with poetry:

**Pre-requisites**

- pip
- poetry

```
cd src 

# Installing dependencies
$ poetry install
$ poetry shell

$ shiny run app.py
```

You can see the app through localhost http://127.0.0.1:8000

To stop running Press Ctrl + C

To stop virtual env 
```
$ exit
```

## Run on virutal environment with Conda

**Pre-requisites**

- mamba or conda

```
cd src 

$ mamba env create --file conda/env.yml
```
You can use conda instead of mamba `$ conda env create --file conda/env.yml`

To activate virutal env and run the app

```
$ conda activate shinyapp

$ shiny run app.py
```

You can see the app through localhost http://127.0.0.1:8000

## Run with Docker 

```
docker build -t shiny:v0.0.1 .
docker run -p 8081:80 -it shiny:v0.0.1
```