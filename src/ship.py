class Ship:
    def __init__(self, draft, crew):
        self.crew=crew
        self.draft=draft


    def is_worth_it(self):
        peso=(self.draft)-(self.crew*1.5)
        if peso<20:
            raise Exception("el botin es menor a 20")
        return peso

