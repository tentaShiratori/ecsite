FROM python:3
ENV POETRY_HOME="/opt/poetry" 
RUN curl -sSL https://install.python-poetry.org/ | python -
RUN mkdir /code
WORKDIR /code
COPY ./pyproject.toml /code
COPY ./poetry.lock /code
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN poetry install --no-dev