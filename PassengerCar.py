from Car import Car

class PassengerCar(Car):
    def __init__(self, plate, rental_fee):
        super().__init__(plate, rental_fee)
        self.car_type = "Személyautó"
