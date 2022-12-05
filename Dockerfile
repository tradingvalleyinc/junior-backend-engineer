# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_DEBUG=1
ENV FLASK_APP=run.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]