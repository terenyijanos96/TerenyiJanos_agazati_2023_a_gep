import minosites
import sorozat

minosites.adatbekeres()
lista = sorozat.veletlen_szam_generator()

db = sorozat.oszthatoak_szama(lista)
sorozat.konzolra_ir(db)
sorozat.fajl_ir(db)