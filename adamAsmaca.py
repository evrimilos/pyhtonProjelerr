import random

textFile = open(r"word.txt",'r').readline()
textList = textFile.split(",")

randomNumber = random.randint(0,len(textList) -1)
selectedWord = textList[randomNumber]
lives = 6

letterList = ["_"] *len(selectedWord)
letterNumber = "selected word has " +  str(len(selectedWord)) + " letters"
print(letterNumber)

while True:
    #kelimeyi gizle 
    print(" ".join(letterList))
    
    guess = input("enter letter: ")
    
    #eğer seçilen harf kelimede varsa kelimede nere olduğunu göster
    if guess in selectedWord:
        for i in range(len(selectedWord)):
            if selectedWord[i] == guess:
                letterList[i] = guess
        print(" \nCorrect guess!" )
        print ("Lives left: " + str(lives))
        
        #bütün harfler bilindiğinde oyun bitiyor
        if "_" not in letterList:
            print("Congratulations you WON, Word was: " + selectedWord)
            break

    #yanlış tahmin yapıldığında candan 1 eksiltiyor
    else:
     lives -= 1
     print ("\nWrong guess")
     print ("Lives left: " + str(lives))

    #canlar sıfırlandığında oyun bitiyor
    if lives == 0:
        print ("Game over, Word was: " + selectedWord)
        break