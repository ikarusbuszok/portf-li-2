import Csoprt
def elso():
    adatokLista = []

    def beolvas():
         beFajl=open("evfolyam.txt", "r", encoding="utf-8")
         beFajl.readline()
         adatok=beFajl.readlines()
         index=0
         while index < len(adatok):
             tisztitottSor = adatok[index].strip()
             adatok[index].strip()
             tanulo=Csoprt.Csoprt(tisztitottSor)
             adatokLista.append(tanulo)
             index += 1
             beFajl.close()

             def kiir():
                 index = 0
                 while index < len(adatokLista):
                     print(f"{adatokLista[index]}")
                     index += 1

                     beolvas()
                     kiir()
                     def legnagyobbAtlag():
                         maxErtek=adatokLista[0].atlag
                         index = 0
                         while index < len(adatokLista):
                             if maxErtek < adatokLista[index].atlag:
                                 maxErtek = adatokLista[index]. atlag








