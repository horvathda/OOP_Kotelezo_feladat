from CarRental import CarRental
from PassengerCar import PassengerCar
from Truck import Truck
from datetime import date, datetime


class CarRentalSystem:

    def __init__(self):
        self._car_rental = CarRental("Hol a lé Kft.")
        self._init_data()


    def _init_data(self):
        self._car_rental.cars =PassengerCar("ABC-123",10000)
        self._car_rental.cars =PassengerCar("ABC-456", 12000)
        self._car_rental.cars =PassengerCar("ABC-789",14000)
        self._car_rental.cars =Truck("DEF-123",20000)
        self._car_rental.cars =Truck("DEF-456",22000)

        self._car_rental.rent_by_plate("ABC-123", date(2025, 5, 5))
        self._car_rental.rent_by_plate("ABC-456", date(2025, 5, 5))
        self._car_rental.rent_by_plate("DEF-123", date(2025, 5, 5))

    def user_interact(self):
        while True:
            print("1. Autók listázása")
            print("2. Foglalások listázása")
            print("3. Autó foglalás")
            print("4. Foglalás lemondása")
            print ("5. Kilépés")
            try:
                choice = int(input("Válasszon a menüpontok közül:"))
            except ValueError:
                print("Kérem csak számot adjon meg!")
                continue


            if choice == 1 :
                self._car_rental.cars

            elif choice == 2:
                self._car_rental.rentals

            elif choice == 3:


                while True:

                    user_in = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")

                    try:

                        rental_date = datetime.strptime(user_in, "%Y-%m-%d").date()

                    except ValueError:

                        print("Hibás formátum! Kérem YYYY-MM-DD formátumot adjon meg!")

                        continue

                    if rental_date < date.today():
                        print("A dátum nem lehet múltbéli!")

                        continue

                    break


                available_cars = []

                for car in self._car_rental._cars:
                    is_busy = False
                    for p, d in self._car_rental._rentals:
                        if p == car.plate and d == rental_date:
                            is_busy = True
                            break

                    if not is_busy:
                        available_cars.append(car)

                if len(available_cars) == 0:
                    print(f"Nincsenek szabad autók erre a napra: {rental_date}")

                    continue


                print("Szabad autók ezen a napon:")

                for car in available_cars:
                    print(f"  {car.plate} – {car.car_type}, {car.rental_fee} HUF")


                while True:

                    plate_input = input("Adja meg annak az autónak a rendszámát, amit le szeretne foglalni: ").upper()
                    found_in_available = False

                    for car in available_cars:
                        if car.plate == plate_input:
                            found_in_available = True
                            break

                    if found_in_available:
                        plate = plate_input
                        break

                    found_in_fleet = False

                    for car in self._car_rental._cars:

                        if car.plate == plate_input:
                            found_in_fleet = True

                            break

                    if found_in_fleet:

                        print(f"A {plate_input} rendszámú autó erre a napra {rental_date} nem foglalható már.")

                    else:

                        print(f"Nincs ilyen rendszámú autónk: {plate_input}")


                self._car_rental.rent_by_plate(plate, rental_date)
                print(f"Sikeres foglalás: {plate} – {rental_date}")

            elif choice == 4:



                while True:

                    user_in = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")

                    try:

                        rental_date = datetime.strptime(user_in, "%Y-%m-%d").date()

                    except ValueError:

                        print("Hibás formátum! Kérem YYYY-MM-DD formátumot adjon meg!")

                        continue

                    if rental_date < date.today():
                        print("A dátum nem lehet múltbéli!")

                        continue

                    break


                busy_cars = []

                for car in self._car_rental._cars:
                    is_busy = False
                    for p, d in self._car_rental._rentals:
                        if p == car.plate and d == rental_date:
                            is_busy = True
                            break

                    if is_busy:
                        busy_cars.append(car)

                if len(busy_cars) == 0:
                    print(f"Nincsenek foglalt autók erre a napra: {rental_date}")

                    continue


                print("Foglalt autók ezen a napon:")

                for car in busy_cars:
                    print(f"  {car.plate} – {car.car_type}, {car.rental_fee} HUF")


                while True:

                    plate_input = input("Adja meg annak az autónak a rendszámát, amit le szeretne mondani: ").upper()
                    found_in_busy = False

                    for car in busy_cars:
                        if car.plate == plate_input:
                            found_in_busy = True
                            break

                    if found_in_busy:
                        plate = plate_input
                        break

                    found_in_fleet = False

                    for car in self._car_rental._cars:

                        if car.plate == plate_input:
                            found_in_fleet = True

                            break

                    if found_in_fleet:

                        print(f"A {plate_input} rendszámú autó erre a napra {rental_date} szabad.")

                    else:

                        print(f"Nincs ilyen rendszámú autónk: {plate_input}")


                self._car_rental.unrent_by_plate(plate, rental_date)



            elif choice == 5:
                print("Viszontlátásra!")
                break

            else:
                print("Hibás menüpont próbálja újra")
                continue



CarRentalSystem = CarRentalSystem()
CarRentalSystem.user_interact()