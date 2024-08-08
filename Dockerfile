FROM python:3.10-slim

RUN pip install poetry

COPY . /hw_09

WORKDIR /hw_09

RUN poetry install

VOLUME /hw_09/allure-results

ENTRYPOINT ["poetry", "run", "pytest", "--alluredir=/hw_09/allure-results"]

