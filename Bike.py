class Bike:
    PRICES = {"REGULAR": 2, "ELECTRICAL": 5}

    def __init__(self, number, bike_type, charge=100):
        self.number = number
        self.bike_type = bike_type
        self.charge = charge

    def get_trip_price(self, minutes):
        return minutes * self.PRICES[self.bike_type]

    def is_usable(self):
        return self.bike_type != "ELECTRICAL" or self.charge >= 20
