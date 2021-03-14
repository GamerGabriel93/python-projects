from datetime import date
from datetime import datetime


class Schedule:
    #értékek kinyerése a számítógépből
    def current_time(self):
        day = date.today()
        time = datetime.now()
        return day.strftime("%Y.%m.%d"), time.strftime("%H:%M")


class Timerecord:
    def arrival(self):
        arrive = Schedule()
        return arrive.current_time()

    def leaving(self):
        leave = Schedule()
        return leave.current_time()
