from distutils.log import debug
from flask import Flask, request
from flask_restful import Api, Resource
import logging
import json

app = Flask(__name__)
api = Api(app)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(message)s')


class HelloWorld (Resource):
    def post(self):
        app.logger.info(request.get_json())
        return ({"data": request.get_json()}, 201)


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
