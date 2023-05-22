class SeznamPojisteny:
    def __init__(self):
        self.seznam = []
        
    def pridej_pojisteneho(self, pojisteny):
        self.seznam.append(pojisteny)
        
    def zobraz_seznam(self):
        for pojisteny in self.seznam:
            print(pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.telefon)
            
    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.seznam:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None
