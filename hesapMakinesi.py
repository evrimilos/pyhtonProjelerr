firstNumber=input("Enter first number: ")
print ("firstNumber = ", firstNumber)
secondNumber= input ("Enter second number: ")
print ("secondNumber = ", secondNumber)

operation = input ("yapılacak işlemi seçin : \n 1- Toplama \n 2- Çıkarma \n 3- Çarpma \n 4- Bölme: ")

if operation == '1':
    print(firstNumber, "+", secondNumber, "=", float(firstNumber) + float(secondNumber))
elif operation == '2':
    print(firstNumber, "-", secondNumber, "=", float(firstNumber) - float(secondNumber))   
elif operation == '3':
    print(firstNumber, "*", secondNumber, "=", float(firstNumber) * float(secondNumber))
elif operation == '4':
    print(firstNumber, "/", secondNumber, "=", float(firstNumber) / float(secondNumber))
