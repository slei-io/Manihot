from distutils.log import debug
from flask import Flask
from flask_restful import Api
from core.consumerView import ConsumerView
from time import sleep

app = Flask(__name__)
api = Api(app)


class Main (ConsumerView):
    def task(self, data):
        app.logger.info(data)
        return super().task(data)


api.add_resource(Main, "/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
