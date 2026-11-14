class Client:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.current_bike = None
