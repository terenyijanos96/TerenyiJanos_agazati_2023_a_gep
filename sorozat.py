import random


def veletlen_szam_generator():
    szam_lista = []
    szoveg = ""

    for i in range(13):
        vel = int(random.random() * 591) - 90
        szoveg += f"{vel}{'*' if i < 12 else ''}"
        szam_lista.append(vel)

    print(f"\nII/A, B, C:\n\t{szoveg}")

    return szam_lista


def oszthatoak_szama(lista):
    db = 0
    for i in lista:
        if i % 10 == 0:
            db += 1

    return db

def konzolra_ir(db):
    print(f"II/D, E:\n\tTízzel osztható számok száma: {db}.")

def fajl_ir(db):
    f = open("kimutatas.txt", "w", encoding="utf-8")
    f.write(f"II/F:\n\tTízzel osztható számok száma: {db}.")
    f.close()
