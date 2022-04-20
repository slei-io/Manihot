from flask import request
from flask_restful import Resource
from threading import Thread
from config import app


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
