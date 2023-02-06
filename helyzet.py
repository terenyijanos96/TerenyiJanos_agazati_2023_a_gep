from Szamitogep import *
def adat_bekeres_es_eltarolas_osztalyban():
    f = open("gep.txt", "r", encoding="utf-8")
    tartalom = f.readlines()
    f.close()

    szamitogep_lista = []

    i = 1
    while i < len(tartalom):
        sor = tartalom[i].strip().split("!")
        szamitogep_lista.append(Szamitogep(sor))
        i+=1

    return szamitogep_lista

def gepek_szama(lista):
    kimenet= len(lista)
    print(f"III/A, B:\n\tA gépek száma: {kimenet}.")
    return kimenet

def atlag(lista):
    i = 0
    osszeg = 0
    db = 0
    while i < len(lista):
        terem_id = lista[i].id
        if terem_id % 2 == 0:
            osszeg += terem_id
            db += 1
        i+=1

    kimenet = int(osszeg / db)

    print(f"III/C:\n\tA páros teremszámú termek azonosító átlaga: {kimenet}.")
    return kimenet

def legkisebb_azonositoju_asztali_gep(lista):
    i = 0
    while i < len(lista) and lista[i].tipus != "asztali":
        i+=1


    if i < len(lista):
        sz_id = lista[i].id
        sz_hely = lista[i].hely
    else:
        sz_id = "NULL"
        sz_hely = "NULL"

    print(f"III/D:\n\tA legkisebb asztali gép azonosítója: {sz_id}, helye: {sz_hely}.")
