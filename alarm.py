import datetime as dt
from datetime import datetime
from datetime import time
from kivy.core.audio import SoundLoader

from alarm_exception import AlarmException


class Alarm:
    def __init__(self, ringTime: datetime = datetime.now() + dt.timedelta(hours=1), melody="resources/ring1.mp3", repeat=False):
        self._ringTime = ringTime
        self._melody = melody
        self._repeat = repeat
        self._player = SoundLoader.load(melody)
        self._player.loop = True

    @property
    def repeat(self):
        return self._repeat

    @repeat.setter
    def repeat(self, on: bool):
        self._repeat = on

    @property
    def volume(self):
        return self._player.volume

    @volume.setter
    def volume(self, value):
        if value < 0 or value > 1:
            raise AlarmException(f"Wrong volume value {value}")
        self._player.volume = value

    def ring(self):
        self._player.play()

    def stopRinging(self):
        self._player.stop()

    def toggle(self):
        print("!")
        if self._player.state == 'play':
            self.stopRinging()
        else:
            self.ring()


if __name__=="__main__":
    pass
