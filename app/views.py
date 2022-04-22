from time import sleep
from core.consumerView import ConsumerView


class Main (ConsumerView):
    def task(self, data):
        sleep(10)
        return super().task(data)
