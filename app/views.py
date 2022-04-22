from time import sleep
from core.consumerView import ConsumerView


class Main (ConsumerView):
    def task(self, data):
        sleep(5)
        return super().task(data)
