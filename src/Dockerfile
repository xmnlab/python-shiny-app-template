FROM python:3.10.9-buster
RUN pip install poetry==1.2.2
workdir /src
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock
RUN poetry config virtualenvs.create false && \ 
poetry install
COPY ./app.py ./app.py
CMD ["poetry","run","shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "80"]