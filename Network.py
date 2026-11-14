class Network():
    def __init__(self, stations: dict):
        self.stations = stations

    def get_stations(self):
        return self.stations

    def get_profit(self):
        profit = 0
        for station, balance in self.stations.items():
            if balance > 0:
                profit += balance
        return profit