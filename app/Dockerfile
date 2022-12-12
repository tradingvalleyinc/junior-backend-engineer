FROM python:3.11.1-alpine

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
CMD [ "python", "main.py", "--reload", "--debugger", "--host", "0.0.0.0", "--port", "5001" ]
