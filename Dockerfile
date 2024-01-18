FROM python:3.11.2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements1.txt /app/

RUN pip install --upgrade pip && pip install -r requirements1.txt

COPY . /app/

EXPOSE 8000

RUN python manage.py collectstatic --noinput

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
