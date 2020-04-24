FROM python:3.6

ARG PROJECT_DIR="/backend"

COPY . ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000

EXPOSE 8000