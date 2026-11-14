class Client:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.current_bike = None

    def rent_bike(self, type, station, minutes):
        if self.current_bike:
            return "already_renting"

        bike = station.get_bike(type)
        if not bike:
            low = any(b.bike_type == type and not b.is_usable() for b in station.bikes)
            return "low_charge" if low else "no_bike"

        price = bike.get_trip_price(minutes)
        if price > self.balance:
            station.add_bike(bike)
            return "no_money"

        self.balance -= price
        station.add_balance(price)
        self.current_bike = bike
        return "ok"

    def return_bike(self, station):
        if self.current_bike:
            station.add_bike(self.current_bike)
            self.current_bike = None

    def add_to_balance(self, money):
        if money < 0:
            return
        self.balance += money
