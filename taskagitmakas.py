# taş=0 kağıt=1 makas=2
import random

skorOyuncu = 0
skorBilgisayar = 0

while True:

    computer = random.randint(0,2)
    user = input("seçim yap: ")
    
    if( int(user) == 1):
        if (computer == 0):
            skorOyuncu += 1
        if (computer == 1):
            pass
        if (computer == 2):
            skorBilgisayar += 1
    
    if( int(user) == 0):
        if (computer == 0):
            pass 
        if (computer == 1):
            skorBilgisayar +=1
        if (computer == 2):
            skorOyuncu +=1
    
    if( int(user) == 2):
        if (computer == 0):
            skorBilgisayar += 1
        if (computer == 1):
            skorOyuncu += 1
        if (computer == 2):
            pass

    print(computer)
    print("oyuncu skoru: %s bilgisayar skoru :" %skorOyuncu , skorBilgisayar)

    if(skorOyuncu == 3):
        print("oyuncu kazandı.")
        break
    if(skorBilgisayar == 3):
        print("bilgisayar kazandı.")
        break
