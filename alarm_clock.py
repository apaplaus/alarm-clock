from alarm import Alarm
from alarm_exception import AlarmException

class AlarmClock:
    def __init__(self, maxCapacity=10):
        self.__currentId = 0
        self.__alarms = {}
        self.__maxCapacity = maxCapacity

    def addAlarm(self, alarm: Alarm):
        if len(self.__alarms) >= self.__maxCapacity:
            raise AlarmException("Too many alarms, sorry :(")

        self.__alarms[self.__currentId] = alarm
        self.__currentId += 1
        return self.__currentId - 1

    def delAlarm(self, alarmID: int):
        if self.__alarms.pop(alarmID, None) is None:
            raise AlarmException(f"Can't find Alarm with ID {alarmID}")

    def getAlarm(self, alarmID: int):
        tempAlarm = self.__alarms.get(alarmID, None)
        if tempAlarm is None:
            raise AlarmException(f"There is no Alarm with ID {alarmID}")
        return tempAlarm

    def getAllAlarms(self):
        return self.__alarms
