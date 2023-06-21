FROM python:alpine3.14
RUN apk add --no-cache --upgrade bash
RUN apk add --no-cache tzdata
ENV TZ America/Toronto
RUN pip3 install flask requests requests-oauthlib

RUN mkdir -p /app/Authenticate/src
WORKDIR /app/Authenticate/src

ENTRYPOINT ["flask", "--app", "server", "run", "--debug", "--host", "0.0.0.0", "--port", "80"]
