import datetime as dt
from datetime import datetime
from datetime import time

class Alarm:
    def __init__(self, ringTime: datetime = datetime.now() + dt.timedelta(hours=1), melody="default", repeat=False):
        self._ringTime = ringTime
        self._melody = melody
        self._repeat = repeat

    @property
    def repeat(self):
        return self._repeat

    @repeat.setter
    def repeat(self, on: bool):
        self._repeat = on


    def ring(self):
        pass

    def stopRinging(self):
        pass