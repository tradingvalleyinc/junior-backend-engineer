FROM python

WORKDIR /home/app

COPY . /home/app

COPY ./requirements.txt /home/app/requirements.txt

RUN pip3 install --upgrade -r ./requirements.txt

CMD [ "python3", "app.py", "--host", "0.0.0.0", "--port","5000" ]