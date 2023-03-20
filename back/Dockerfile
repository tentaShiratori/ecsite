FROM python:3.11
ENV POETRY_HOME="/opt/poetry" 
RUN curl -sSL https://install.python-poetry.org/ | python -
RUN mkdir /code
WORKDIR /code
COPY ./pyproject.toml /code
COPY ./poetry.lock /code
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN poetry install --only main
COPY . /code
CMD ["poetry","run","gunicorn", "--bind", "0.0.0.0:8000", "ecsite.wsgi"]
