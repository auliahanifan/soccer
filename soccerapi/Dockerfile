FROM python:3.7.9
COPY . /app
WORKDIR /app
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
# RUN python manage.py migrate
# RUN python manage.py migrate team
# RUN python manage.py test
# CMD ["python", "manage.py", "runserver"]
