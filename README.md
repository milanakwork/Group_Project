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
| ------- | --------------------------- |------------------------------------------------------------------|
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
