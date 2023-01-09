class Konyv:
    def __init__(self, sor):
        daraboltSor=sor.split("*")
        self.szerzo=daraboltSor[0]
        self.mCim=daraboltSor[1]
        self.peldany=int(daraboltSor[2])
        self.ev=int(daraboltSor[3])

        def __str__(self):
            return f"szerző: {self.szerzo}"
