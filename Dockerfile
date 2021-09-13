FROM python:3.9
WORKDIR /log_generator/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "./main.py"]