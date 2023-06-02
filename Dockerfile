FROM python:3.10.10-bullseye

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /workspace

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]