from datetime import datetime


class Schedule:
    #értékek kinyerése a számítógépből
    def current_time(self):
        daytime = datetime.now()
        day = daytime.strftime("%Y.%m.%d")
        time = daytime.strftime("%H:%M")
        daytime = {"date": day, "time": time}
        return daytime


class Timerecord:
    def arrival(self):
        arrive = Schedule()
        return arrive.current_time()

    def leaving(self):
        leave = Schedule()
        return leave.current_time()
