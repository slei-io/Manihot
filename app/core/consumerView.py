import imp
from flask import request
from flask_restful import Resource
from threading import Thread
from config import app
from os import environ
import requests as res
from http import HTTPStatus


class ConsumerView(Resource):
    default_success_code = HTTPStatus.ACCEPTED

    def post(self):
        data = self.serialize(request.get_json())
        thread = Thread(target=self._try_task, args=[data], daemon=True)
        thread.start()
        return self.set_payload(data), self.default_success_code

    def set_payload(self, data):
        return data

    def _try_task(self, data):
        try:
            self.task(data)
        except Exception as err:
            self.set_task_error(data, err)

    def set_task_error(self, data, err):
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
