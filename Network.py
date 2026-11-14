from Station import Station


class Network:
    def __init__(self):
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self):
        return self.stations

    def get_profit(self):
        return sum(station.balance for station in self.stations)

    def get_low_charge(self):
        return [(b, s) for s in self.stations for b in s.bikes if not b.is_usable()]