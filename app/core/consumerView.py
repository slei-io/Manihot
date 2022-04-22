from flask import request
from flask_restful import Resource
from threading import Thread
from core.serializers import Serializer
from core.manihot import app
from os import environ
import requests as res
from http import HTTPStatus


class ConsumerView(Resource):
    default_success_code = HTTPStatus.ACCEPTED

    def get_serializer_class(self):
        return Serializer

    def get_serializer(self, data):
        serializer_class = self.get_serializer_class()
        return serializer_class(data=data)

    def post(self):
        data = self.serialize(request.get_json())
        thread = Thread(target=self._try_task, args=[data], daemon=True)
        thread.start()
        return self.get_payload(data), self.default_success_code

    def get_payload(self, data):
        return self.get_serializer(data).get_data()

    def _try_task(self, data):
        try:
            self.task(data)
        except Exception as err:
            self.save_task_error(err, data)

    def save_task_error(self, err, data):
        app.logger.error(f'{err}, when running task on: {data}')

    def serialize(self, data):
        return data

    def task(self, data):
        app.logger.info(data)


class HttpGatewayConsumerView(ConsumerView):
    def get_write_url(self):
        return environ.get('DATA_WRITE_URL')

    def get_token(self):
        return environ.get('DATA_WRITE_TOKEN')

    def get_headers(self):
        token = self.get_token()
        return {'Authorization': f'Token {token}'}

    def task(self, data):
        url = self.get_write_url()
        headers = self.get_headers()
        response = res.post(url, data=data, headers=headers)
        self.log(data=data, response=response)

    def log(self, data, response):
        app.logger.info(f'{response.status_code} - {data}')
