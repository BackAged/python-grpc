FROM python:3.8

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /tmp/myapp

# RUN pip install /tmp/myapp

EXPOSE 3000

CMD ["python", "/tmp/myapp/app.py"]