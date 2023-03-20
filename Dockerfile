FROM python:3.10.10-bullseye

WORKDIR /BirthDayTracker

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]