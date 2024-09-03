def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

lista = [1,2,3,4,5,6]
summa = laske_summa(lista)
print(f"Listan lukujen summa on: {summa}")