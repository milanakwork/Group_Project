class Station:

    def __init__(self):
        self.bikes = []
        self.balance = 0

    def get_bike(self, type):
        for bike in self.bikes:
            if bike.bike_type == type:
                self.bikes.remove(bike)
                return bike

        return None

    def add_bike(self, bike):
        self.bikes.append(bike)

    def add_balance(self, money):
        if money < 0:
            return

        self.balance += money
