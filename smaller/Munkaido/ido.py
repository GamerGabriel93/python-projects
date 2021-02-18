from datetime import date
from datetime import datetime


class Schedule:
    def current_time(self):
        day = date.today()
        time = datetime.now()
        return day.strftime("%Y.%m.%d"), time.strftime("%H:%M:%S")


class Idopontok:
    def erkezes(self):
        arriving = Schedule()
        return arriving.current_time()

    def tavozas(self):
        tavoz = Schedule()
        return tavoz.current_time()
