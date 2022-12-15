FROM python

COPY . /home/app

WORKDIR /home/app

RUN pip3 install --upgrade -r ./requirements.txt

CMD [ "python3", "app.py" ]