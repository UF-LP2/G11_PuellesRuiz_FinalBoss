class Ship:
    def __init__(self, draft, crew):
        self.crew=crew
        self.draft=draft


    def is_worth_it(self):
        peso=(self.draft)-(self.crew*1.5)
        if peso<20:
            raise Exception("el botin es menor a 20")
        return peso

class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers=passengers
        super().__init__(draft, crew)

    def is_worth_it(self):
        peso=(self.draft)-(self.passengers*2.25)-(self.crew*1.5)
        if peso<20:
            raise Exception("el botin es menor a 20")
        return peso


class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo=cargo
        self.quality=quality
        super().__init__(draft, crew)
        
    def is_worth_it(self):
        peso= self.draft
        if self.quality==1 :
            peso=peso+3.5
        elif self.quality==0.5:
            peso=peso+2
        elif self.quality==0.25:
            peso=peso+0.5
        peso= peso- (self.crew*1.5)
        if peso<20:
            raise Exception("el botin es menor a 20")
        return peso
