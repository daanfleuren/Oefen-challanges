
def fullcode():
    invoer = input("voer je zin in:")

    invoer = invoer.replace(" ", "")
    invoer = invoer.lower()
    invoer = invoer.replace("!","")
    invoer = invoer.replace(",","")
    invoer = invoer.replace(".","")
    invoer = invoer.replace("?","")
    invoer = invoer.replace("'","")
    invoer = invoer.replace('"',"")
    invoer = invoer.replace('“',"")


    invoerbackwards = invoer[::-1]
        
    print(invoer)  
    print(invoerbackwards)

    if invoer == invoerbackwards:
        print("het is een palindroom!!!!")

    else:
        print("Het is helaas geen palindroom")

while True:
    fullcode()