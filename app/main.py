from distutils.log import debug
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld (Resource):
    def get(self):
        return {"data": "hello world"}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
