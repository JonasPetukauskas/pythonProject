

def getchange(total_amount, price):
    nominals = [1, 2, 5, 10, 20, 50, 100]
    coin_kiekis = [0, 0, 0, 0, 0, 0, 0]
    kaupiamasis = 0
    count100 = 0
    count50 = 0
    count20 = 0
    count10 = 0
    count5 = 0
    count2 = 0
    count1 = 0

    if total_amount == 0 or price == 0:
        print("Ivesta nuline reiksme, Exiting..")
    elif total_amount < price:
        print("Prekes kaina didesne uz pinigu suma")
        return
    else:
        graza = total_amount - price
        print(f"Jūsų grąža: {round(graza,2)} Eur")
        graza_centais = total_amount*100 - price*100
        # print(f"Jusu graza: {int(graza_centais)} ct")

    likutis = graza_centais


    while likutis>= 100:
        kaupiamasis = kaupiamasis + nominals[6]
        count100+=1
        coin_kiekis[6] = count100
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 100

    while likutis < 100 and likutis >= 50:
        kaupiamasis = kaupiamasis + nominals[5]
        count50=count50+1
        coin_kiekis[5] = count50
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 50

    while likutis < 50 and likutis >= 20:
        kaupiamasis = kaupiamasis + nominals[4]
        count20+=1
        coin_kiekis[4] = count20
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 20

    while likutis < 20 and likutis >= 10:
        kaupiamasis = kaupiamasis + nominals[3]
        count10+=1
        coin_kiekis[3] = count10
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 10

    while likutis < 10 and likutis >= 5:
        kaupiamasis = kaupiamasis + nominals[2]
        count5+=1
        coin_kiekis[2] = count5
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 5

    while likutis < 5 and likutis >= 2:
        kaupiamasis = kaupiamasis + nominals[1]
        count2+=1
        coin_kiekis[1] = count2
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 2

    while likutis < 2 and likutis >= 1:
        kaupiamasis = kaupiamasis + nominals[0]
        count1+=1
        coin_kiekis[0] = count1
        # print(list(coin_kiekis))
        # print("Grazinta:", kaupiamasis, "ct")
        likutis = likutis - 1

    print(f"Grazinama nominalais [1ct, 2ct, 5ct, 10ct, 20ct, 50ct, 1 Eur] : {list(coin_kiekis)}")

while True:
    try:
        price = float(input("Iveskite prekes kaina Eur:"))
        total_amount = float(input("Iveskite paduodama pinigų suma Eur:"))
        getchange(total_amount, price)
        continue
    except ValueError:
        print("Iveskite realius skaicius naudojant . ")
        continue

#getchange(total_amount, price)
