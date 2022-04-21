from flask import request
from flask_restful import Resource
from threading import Thread
from config import app
from os import environ
import requests as res


class ConsumerView(Resource):
    def post(self):
        data = self.serialize(request.get_json())
        thread = Thread(target=self.task, args=[data], daemon=True)
        thread.start()
        return data, 201

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
