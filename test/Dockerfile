FROM python:alpine3.14
RUN mkdir -p /app/test
WORKDIR /app/test
RUN pip3 install requests requests-oauthlib
CMD [ "python3", "./test.py" ]
