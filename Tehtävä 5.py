def poista_parittomat (lista):
    karsittu_lista = []
    for luku in lista:
        if luku % 2 == 0:
            karsittu_lista.append(luku)
    return karsittu_lista




def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

lista = [1,2,3,4,5,6]
karsittu_lista = poista_parittomat(lista)
summa = laske_summa(lista)
print(f"Lista:{lista}")
print(f"karsittu lista:{karsittu_lista}")