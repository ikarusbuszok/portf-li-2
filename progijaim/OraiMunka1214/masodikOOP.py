import konyv
def beolvas():
    AdatokLista = []
    befajl=open("konyv.txt", "r", encoding="utf-8")
    befajl.readline()
    adatok=befajl.readlines()
    adatok = befajl.readlines()
    index = 0
    while index < len(adatok):
        # adatok tisztítása
        tisztitottSor = adatok[index].strip()
        # objektum lérehozása
        tanulo = konyv.konyv(tisztitottSor)
        # listába fűzöm
        AdatokLista.append(tanulo)
        index += 1
    befajl.close()


def kiir():
    index = 0
    while index < len(AdatokLista):
        print(f"{AdatokLista[index]}")
        index += 1

    # főprogram


beolvas()
kiir()
