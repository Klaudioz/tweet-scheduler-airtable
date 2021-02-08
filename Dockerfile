FROM python:3.9.1-alpine3.13

ADD tweet-scheduler.py /

RUN pip install airtable twitter

CMD [ "python", "./tweet-scheduler.py" ]