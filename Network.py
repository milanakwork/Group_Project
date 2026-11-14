class Network():
    def __init__(self, stations: dict, balance: float):
        self.balance = balance
        self.stations = stations

    def get_balance(self):
        return self.balance

    def get_stations(self):
        return self.stations

    def add_balance(self, amount:float):
        if amount > 0:
            return (self.balance + amount)