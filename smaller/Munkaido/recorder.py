from datetime import date
from datetime import datetime


class Schedule:
    def current_time(self):
        day = date.today()
        time = datetime.now()
        return day.strftime("%Y" + " " + "%m" + " " + "%d"), time.strftime("%H:%M")
