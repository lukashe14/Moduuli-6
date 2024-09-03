import math

def laske_yksikkohinta(halkaisija: float, hinta: float) -> float:
    säde = halkaisija / 2
    pinta_ala_m2 = (math.pi * säde**2) / 10000  # Pinta-ala neliömetreinä
    yksikkohinta = hinta / pinta_ala_m2
    return yksikkohinta


halkaisija1 = int(input("Anna halkaisija:"))
hinta1 = int(input("Anna hinta:"))


halkaisija2 = int(input("Anna halkaisija:"))
hinta2 = int(input("Anna hinta:"))


yksikköhinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikköhinta2 = laske_yksikkohinta(halkaisija2, hinta2)

if yksikköhinta1 < yksikköhinta2:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif yksikköhinta2 < yksikköhinta1:
    print("Ensimmäinen pizza on parempi vastine rahalle.")

else:
    print("Molemmilla pizzoilla on sama yksikköhinta.")