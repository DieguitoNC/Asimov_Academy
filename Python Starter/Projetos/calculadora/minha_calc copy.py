another_operation = 0

while another_operation <= 0:


    print("Digite a operação que deseja escolher")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Exponenciação")

    chosen_operation = int(input())


    def sum(a,b):
        return a+b

    def minus(a,b):
        return a-b


    def multiplication(a,b):
        return a*b

    def exponentiation(a,b):
        return a**b

    print("Digite o primeiro número: ")
    number1 = int(input())
    print("Digite o segundo numero: ")
    number2 = int(input())
    
    if chosen_operation == 1:
        result = sum(number1,number2)
        print("O resultado da soma é {}".format(result))
    elif chosen_operation == 2:
        result = minus(number1,number2)
        print("O resultado da subtração é {}".format(result))
    elif chosen_operation == 3:
        result = multiplication(number1,number2)
        print("O resultado da multiplicação é {}".format(result))
    elif chosen_operation == 4:
        result = exponentiation(number1,number2)
        print("O resultado da exponenciação é {}".format(result))
    else:
        print("Digite algo válido")
    
    print("Deseja fazer outra operação? ")
    print("Digite 1 - Para outra operação")
    print("Digite 0 - Para encerrar")
    
    choosen_another_operation = int(input())
    
    if choosen_another_operation == 1:
        another_operation == 0
    else:
        another_operation =+ 1



    
    