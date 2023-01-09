class Szarvas:
    def __init__(self, nev):
        daraboltNev = nev.split("/")
        self.nev = daraboltNev[0]
        self.evfolyam = int(
            daraboltNev[1])
        atlag = daraboltNev[
            2].replace(",", ".")
        self.atlag = float(atlag)

        def __str__(self):
            return f"Név: {self.nev}, évfolyam: {self.evfolyam} átlag: {self.atlag}."