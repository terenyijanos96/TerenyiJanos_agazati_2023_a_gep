import minosites
import sorozat
import helyzet

minosites.adatbekeres()
lista = sorozat.veletlen_szam_generator()

db = sorozat.oszthatoak_szama(lista)
sorozat.konzolra_ir(db)
sorozat.fajl_ir(db)

sz_lista = helyzet.adat_bekeres_es_eltarolas_osztalyban()
helyzet.gepek_szama(sz_lista)
helyzet.atlag(sz_lista)
helyzet.legkisebb_azonositoju_asztali_gep(sz_lista)