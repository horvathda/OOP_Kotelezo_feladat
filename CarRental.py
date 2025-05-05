class CarRental:
    def __init__(self, name):
        self._name = name
        self._cars = []
        self._rentals = []

    @property
    def cars(self):
        for car in self._cars:
            print(f"Rendszám: {car.plate}, Típus: {car.car_type}, Ár: {car.rental_fee} HUF")

    @cars.setter
    def cars(self, new_car):
        self._cars.append(new_car)

    @property
    def rentals(self):
        if not self._rentals:
            print("Nincsenek aktív foglalások.")
            return
        for plate, dt in self._rentals:
            print(f"{plate}: {dt}")

    def rent_by_plate(self, plate, rental_date):
        self._rentals.append((plate, rental_date))

    def unrent_by_plate(self, plate, rental_date):

            self._rentals.remove((plate, rental_date))
            print(f"Foglalás törölve: {plate} – {rental_date}")

