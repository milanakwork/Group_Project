class Bike:
    PRICES = {"REGULAR": 2, "ELECTRICAL": 5}

    def __init__(self, number, bike_type):
        self.number = number
        self.bike_type = bike_type


    def get_trip_price(self, minutes):
        return minutes * self.PRICES[self.bike_type]