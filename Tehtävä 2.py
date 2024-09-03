import random

def heitä_noppaa(tahkojen_määrä: int):
    return random.randint(1,tahkojen_määrä)

tahkojen_määrä = int(input("Syötä tahkojen määrä:"))

maksimi_silmäluku = int(input("Anna maksimi silmäluku:"))

while True:
    noppa = heitä_noppaa(tahkojen_määrä)
    print(f"silmäluvuksi saatiin: {noppa}")

    if noppa == maksimi_silmäluku:
        break
