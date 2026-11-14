class Client:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.current_bike = None

    def rent_bike(self, type, station, minutes):
        bike = station.get_bike(type)
        if not bike or self.current_bike:
            return

        price_need = bike.get_trip_price(minutes)
        if price_need > self.balance:
            station.add_bike(bike)
            return

        station.add_balance(price_need)
        self.current_bike = bike
        self.balance -= price_need

    def add_to_balance(self, money):
        if money < 0:
            return
        self.balance += money
