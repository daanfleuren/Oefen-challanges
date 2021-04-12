def fullcode():
    # code word zo vaak uitgevoerd totdat er (input) geldige BSN's zijn

    try:
        BSNcounter = int(input("Hoeveel BSN's?: "))
    except:
        print("Geef een getal op!")
        return()

    while BSNcounter > 0:
        import random

        y = 0
        h = 0
        BSN = []
        BSNcheck = 0
        BSNMultiply = 9
        
    # list maken van 9 random nummers (BSN)

        while y < 9:
            z = int(random.randint(1,9))
            BSN.append(z)    
            y += 1

    # rekensom voor BSN Check
        while h < 8:
            BSNcheck = BSNcheck + (BSN[h] * BSNMultiply)
            h += 1
            BSNMultiply -= 1

        BSNcheck += (BSN[8] * -1)

    # waneer BSNcheck goed is gegaan
        if BSNcheck % 11 == 0:
            #alle nummers uit list na elkaar printen
            for o in range(9):
                print(BSN[o], end="")
            #niewe regel maken
            print("")
            # 1 afhalen aan BSN counter
            BSNcounter = BSNcounter - 1
            
while True:
    fullcode()
