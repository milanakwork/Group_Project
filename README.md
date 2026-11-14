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

| Class   | Attributes                  | Methods                                                                                |
| ------- | --------------------------- | -------------------------------------------------------------------------------------- |
| Client  | name, balance, current_bike | rent_bike(self, type, station, minutes), return_bike(self, station)                    |
| Station | bikes, balance              | get_bike(self, type), add_bike(self, bike), add_balance(self, money)                   |
| Bike    | number, bike_type, charge   | get_trip_price(self, minutes), is_usable(self)                                         |
| Network | stations                    | add_station(self, station), get_stations(self), get_profit(self), get_low_charge(self) |

## Files and Structure

| Role  | Responsible for                | Responsible person |
| ----- | ------------------------------ | ------------------ |
| Role1 | Stations and bikes             | Milana Karatash    |
| Role2 | Client, balancem, main         | Hlib Tataryntsev   |
| Role3 | Network and profit calculation | Illia Radkivskyi   |

## Презентація (Presentation): program output

--- Initial state ---
Station A: #1 REGULAR, #6 ELECTRICAL, #2 ELECTRICAL, #3 REGULAR
Station B: #4 ELECTRICAL, #5 REGULAR, #7 ELECTRICAL
Olya balance: 100 UAH
Taras balance: 30 UAH

--- Trips ---
Olya rode ELECTRICAL for 10 min Station A -> Station B, paid 50 UAH upfront
Taras rode REGULAR for 5 min Station A -> Station B, paid 10 UAH upfront
Olya rode REGULAR for 15 min Station B -> Station A, paid 30 UAH upfront
Taras cannot rent ELECTRICAL at Station A: only bikes with low charge (<20%) left, none can be rented
Taras cannot rent ELECTRICAL at Station B: not enough balance for this trip

Olya balance: 20 UAH
Taras balance: 20 UAH

--- Administrator report ---
Station A: 3 bikes
Station B: 4 bikes
Low charge electric bikes:
bike #6, Station A, charge 10%
bike #7, Station B, charge 15%
Network earned in total: 90 UAH

All checks passed

## New Requirements: electric bike charge

Changed (9 places in 5 files):

| File       | Class / function       | Change                                                        |
| ---------- | ---------------------- | ------------------------------------------------------------- |
| Bike.py    | Bike.\_\_init\_\_      | new `charge` parameter and attribute (1)                      |
| Bike.py    | Bike.is_usable         | new method: electric bike with charge < 20 is not usable (2)  |
| Station.py | Station.get_bike       | skip bikes that are not usable (3)                            |
| Network.py | Network.get_low_charge | new method: list of (bike, station) with low charge (4)       |
| Client.py  | Client.rent_bike       | return `"low_charge"` when only low-charge bikes are left (5) |
| main.py    | MESSAGES               | message for `"low_charge"` (6)                                |
| main.py    | report                 | "Low charge electric bikes" block (7)                         |
| main.py    | main                   | demo bikes #6 (10%) and #7 (15%) added (8)                    |
| main.py    | run_checks             | assert that low-charge bikes are #6 and #7 (9)                |

Why this many: the architecture helped. Bike prices and the "can this bike be rented" rule live in Bike, so Station and Client only ask `is_usable()`; the report only needs Network, which already knows all stations. The status-code return values (`"ok"`, `"no_bike"`, `"no_money"`) let Client add a new `"low_charge"` result and main just print its message

What made it harder: Station has no name, so main keeps a station-to-name dict for the report; and `Client.rent_bike` had to look at `station.bikes` to tell "no bikes" from "only low-charge bikes".

## Presentation: blocks

| Block              | Time | Presented by     |
| ------------------ | ---- | ---------------- |
| 1. Architecture    | 45 s | Milana Karatash  |
| 2. Demo            | 45 s | Hlib Tataryntsev |
| 3. New requirement | 40 s | Milana Karatash  |
| 4. Microservice    | 20 s | Hlib Tataryntsev |
