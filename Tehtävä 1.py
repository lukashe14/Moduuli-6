import random

def heitä_noppaa():
    return random.randint(1,6)


while True:
    noppa = heitä_noppaa()
    print(f"silmäluvuksi saatiin: {noppa}")

    if noppa == 6:
        break


