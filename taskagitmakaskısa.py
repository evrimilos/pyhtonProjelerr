# taş=0 kağıt=1 makas=2
import random

skorOyuncu = 0
skorBilgisayar = 0

while True:

    computer = random.randint(0,2)
    user = input("seçim yap: ")

    if( int(user) == int(computer)):
        pass
    
    elif( int(user) == 0 and int (computer) == 2) or \
            (int(user) == 1 and int (computer) == 0) or \
            (int (user) == 2 and int (computer) == 1):
     skorOyuncu +=1

    else: skorBilgisayar +=1

    print(computer)
    print("oyuncu skoru: %s bilgisayar skoru :" %skorOyuncu , skorBilgisayar)
    
    if(skorOyuncu == 3):
        print("oyuncu kazandı.")
        break
    if(skorBilgisayar == 3):
        print("bilgisayar kazandı.")
        break