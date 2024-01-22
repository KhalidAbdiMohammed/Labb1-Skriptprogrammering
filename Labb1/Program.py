import module
while True:
    print("\n Välj ett av alternativen nedan")
    print("1. Gissnigsspelet")
    print("2. Hitta ett tal som är delbart med två egna heltal")
    print("3. Avsluta")

    print("Ange ett tal mellan 1-3")

    val = input()

    if val == "1":
        module.gissningspelet()
    elif val == "2":
        number1 = int(input("Ange det första talet: "))
        number2 = int(input("Ange det andra talet: "))

        resultat = module.egental(number1, number2)

        print(f"Talen mellan 1 och 1600 som är delbart med"
              f" {number1} och {number2} är: {resultat}")

    elif val == "3":
        print("Programmet avslutas, Tack för din tid!")
        break
    else:
        print("Ogiltigt val, vänligen välj en siffra mellan 1-3")

