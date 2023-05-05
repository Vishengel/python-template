FROM arm32v7/python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY pyproject.toml .

COPY python_template python_template

WORKDIR /app/python_template

CMD ["python", "python_template.py"]
