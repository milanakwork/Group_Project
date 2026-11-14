## Nouns and verbs

| Nouns         | Verbs              |
| ------------- | ------------------ |
| Station       |                    |
| Bike          |                    |
| Number        |                    |
| Client        | Rent, ride, return |
| Balance       | Subtract money     |
| Administrator |                    |
| Network       | Earn               |
| Name          | Earn               |

Classes: Station, Bike, Client, Network, Administrator

Properties: station.bikes, bike.type, number, balance, name

Class methods: rent, subtract money

## Classes cards

| Class   | Attributes                  | Methods                                                          |
| ------- | --------------------------- | ---------------------------------------------------------------- |
| Client  | name, balance, current_bike | rent(self, type, station, minutes), return(self, station)        |
| Station | bikes                       | get_bike(self, type), add_bike(self, bike: Bike)                 |
| Bike    | type, price                 | get_trip_price(self, n)                                          |
| Network | stations, balance           | get_balamce(self), get_stations(self), add_balance(self, amount) |

## Files and Structure

| Role  | Responsible for                | Responsible person |
| ----- | ------------------------------ | ------------------ |
| Role1 | Stations and bikes             | Milana Karatash    |
| Role2 | Client, balancem, main         | Hlib Tataryntsev   |
| Role3 | Network and profit calculation | Illia Radkivskyi   |

## Test scenario output

--- Initial state ---
Station A: #1 REGULAR, #2 ELECTRICAL, #3 REGULAR
Station B: #4 ELECTRICAL, #5 REGULAR
Olya balance: 100 UAH
Taras balance: 30 UAH

--- Trips ---
Olya rode ELECTRICAL for 10 min Station A -> Station B, paid 50 UAH upfront
Taras rode REGULAR for 5 min Station A -> Station B, paid 10 UAH upfront
Olya rode REGULAR for 15 min Station B -> Station A, paid 30 UAH upfront
Taras cannot rent ELECTRICAL at Station A: no bikes of this type left at the station
Taras cannot rent ELECTRICAL at Station B: not enough balance for this trip

Olya balance: 20 UAH
Taras balance: 20 UAH

--- Administrator report ---
Station A: 2 bikes
Station B: 3 bikes
Network earned in total: 90 UAH

All checks passed
