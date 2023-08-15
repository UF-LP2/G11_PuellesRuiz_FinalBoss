from src.ship import Ship

class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers=passengers
        super().__init__(draft, crew)

    def is_worth_it(self):
        peso=self.draft-self.passengers*2.25-self.crew*1.5
        if peso<20:
            raise Exception("el botin es menor a 20")
        return peso
