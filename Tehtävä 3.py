def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True:

    määrä = int(input("Anna gallonat:"))

    if määrä < 0:
        break

    litrat = gallonat_litroiksi(määrä)

    print(f"{määrä} gallonaa on litroissa {litrat:.2f}")