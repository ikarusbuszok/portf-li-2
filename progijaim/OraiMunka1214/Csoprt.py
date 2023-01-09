class Csoport:
    def __init__(self,sor):
        daraboltSor=sor.split("/")
        self.nev=daraboltSor[0]
        self.evfolyam=int(
            daraboltSor[1])
        atlag=daraboltSor[
            2].replace(",",".")
        self.atlag=float(atlag)

        def __str__(self):
            return f"Név: {self.nev}, évfolyam: {self.evfolyam} átlag: {self.atlag}."


       
