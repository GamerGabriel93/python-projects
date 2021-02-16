import recorder


class Idopontok:
    def erkezes(self):
        arriving = recorder.Schedule()
        return arriving.current_time()

    def tavozas(self):
        tavoz = recorder.Schedule()
        return tavoz.current_time()
