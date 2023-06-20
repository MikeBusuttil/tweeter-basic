FROM python:alpine3.14
RUN mkdir /app
WORKDIR /app
RUN pip3 install requests requests-oauthlib
CMD [ "python3", "./test.py" ]
