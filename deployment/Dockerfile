FROM python:3.8.10-slim

ENV PYTHONUNBUFFERED=1
ENV WORKDIR /app/

WORKDIR ${WORKDIR}

COPY Pipfile Pipfile.lock ${WORKDIR}

RUN pip3 install pipenv --no-cache-dir

RUN pipenv install --system --deploy --ignore-pipfile

COPY . $WORKDIR

RUN python3 manage.py migrate
