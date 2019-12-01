from src.alarm import Alarm
from src.app_base import MyApp
import unittest


class AlarmTest(unittest.TestCase):
    def testButtonRinging(self):
        testAlarm = Alarm()
        testAlarm.volume = 0.3
        app = MyApp()
        app.pushButton.bind(on_press=lambda x: testAlarm.toggle())
        app.run()



def run():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
