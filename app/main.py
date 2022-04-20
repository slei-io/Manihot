from core.consumerView import ConsumerView
from config import app, api


class Main (ConsumerView):
    def task(self, data):
        app.logger.info(__name__)
        return super().task(data)


api.add_resource(Main, "/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
