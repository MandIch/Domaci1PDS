FROM python

WORKDIR /client

COPY . /client

RUN pip install requests

EXPOSE 80

CMD ["python" , "client.py"]