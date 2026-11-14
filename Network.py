from Station import Station
class Network():
    def __init__(self):
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self):
        return self.stations

    def get_profit(self):
        sum(station.balance for station in self.stations)