from Bike import Bike
from Client import Client
from Network import Network
from Station import Station

MESSAGES = {
    "no_bike": "no bikes of this type left at the station",
    "low_charge": "only bikes with low charge (<20%) left, none can be rented",
    "no_money": "not enough balance for this trip",
    "already_renting": "client already has a bike",
}


def trip(client, bike_type, start, end, minutes, names):
    status = client.rent_bike(bike_type, start, minutes)
    if status != "ok":
        print(f"{client.name} cannot rent {bike_type} at {names[start]}: {MESSAGES[status]}")
        return
    price = client.current_bike.get_trip_price(minutes)
    client.return_bike(end)
    print(
        f"{client.name} rode {bike_type} for {minutes} min "
        f"{names[start]} -> {names[end]}, paid {price} UAH upfront"
    )


def report(network, names):
    print("\n--- Administrator report ---")
    for station in network.get_stations():
        print(f"{names[station]}: {len(station.bikes)} bikes")
    print("Low charge electric bikes:")
    for bike, station in network.get_low_charge():
        print(f"  bike #{bike.number}, {names[station]}, charge {bike.charge}%")
    print(f"Network earned in total: {network.get_profit()} UAH")


def run_checks(network, station_a, station_b, olya, taras):
    # all 7 bikes are back on stations after the trips
    assert sum(len(s.bikes) for s in network.get_stations()) == 7
    # low-charge bikes were never rented
    assert [b.number for b, _ in network.get_low_charge()] == [6, 7]
    # money paid by clients equals network profit
    assert (100 - olya.balance) + (30 - taras.balance) == network.get_profit()
    # returning without a bike does not add a bike to the station
    before = len(station_a.bikes)
    olya.return_bike(station_a)
    assert olya.current_bike is None and len(station_a.bikes) == before


def main():
    network = Network()
    station_a, station_b = Station(), Station()
    names = {station_a: "Station A", station_b: "Station B"}
    network.add_station(station_a)
    network.add_station(station_b)

    for bike in (Bike(1, "REGULAR"), Bike(6, "ELECTRICAL", 10), Bike(2, "ELECTRICAL"), Bike(3, "REGULAR")):
        station_a.add_bike(bike)
    for bike in (Bike(4, "ELECTRICAL"), Bike(5, "REGULAR"), Bike(7, "ELECTRICAL", 15)):
        station_b.add_bike(bike)

    olya = Client("Olya", 100)
    taras = Client("Taras", 30)

    print("--- Initial state ---")
    for station in network.get_stations():
        bikes = ", ".join(f"#{b.number} {b.bike_type}" for b in station.bikes)
        print(f"{names[station]}: {bikes}")
    print(f"Olya balance: {olya.balance} UAH")
    print(f"Taras balance: {taras.balance} UAH")
    print("\n--- Trips ---")

    trip(olya, "ELECTRICAL", station_a, station_b, 10, names)  # 50
    trip(taras, "REGULAR", station_a, station_b, 5, names)  # 10
    trip(olya, "REGULAR", station_b, station_a, 15, names)  # 30
    trip(taras, "ELECTRICAL", station_a, station_b, 10, names)  # only low-charge #6 left at A
    trip(taras, "ELECTRICAL", station_b, station_a, 10, names)  # 50 > 20 balance

    print(f"\nOlya balance: {olya.balance} UAH")
    print(f"Taras balance: {taras.balance} UAH")

    report(network, names)
    run_checks(network, station_a, station_b, olya, taras)
    print("\nAll checks passed")


if __name__ == "__main__":
    main()
