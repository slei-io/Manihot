FROM python:3.9-alpine
LABEL maintainer="Slei"

ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN adduser -D user
USER user

CMD ["entrypoint.sh"]

