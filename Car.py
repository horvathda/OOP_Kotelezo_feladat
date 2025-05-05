from abc import ABC

class Car(ABC):
    def __init__(self, plate, rental_fee):
        self._plate = plate
        self._rental_fee = rental_fee


    @property
    def plate(self):
        return self._plate

    @property
    def rental_fee(self):
        return self._rental_fee

