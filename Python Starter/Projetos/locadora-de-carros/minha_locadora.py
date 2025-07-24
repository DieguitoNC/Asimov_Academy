#choose_car = print("Escolha qual carro você deseja:")

print("==========================")
print("Bem vindo a locadora de carros !")
print("==========================")
print("")
print("O que des0eja fazer ?")
print("")
print("0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro")

choice_portfolio_rent_return = int(input())



car_list_price = {"car1": 70, "Car2": 80, "Car3": 50, "Car4": 110 , "Car5": 200, "Car6": 600}

len_car_list = len(car_list_price)

car_list = list(car_list_price.keys())
price_list = list(car_list_price.values())
number_to_choose = list(range(len_car_list))

if choice_portfolio_rent_return == 0:
    print("Foi escolhido mostrar o portfolio")
    print("")
elif choice_portfolio_rent_return == 1:
    print("")
    print("Foi escolhido alugar um carro")
    print("")
    print("[ ALUGAR ] Dê uma olhada em nosso portfifólio.")
    print("")
    # tem que ter uma lista com o nome e quanto custa cada aluguel no dia
    for k,v,n in zip(car_list, price_list,number_to_choose):
        print("[{}] - {} - R$ {}/ dia".format(n,k,v))
    print("")
    print("===================")
    print("Escolha o código do carro:")
    choose_rented_car = int(input())
    if choose_rented_car <= len_car_list:
        print("Deu good, O NUMERO ESTA NA LISTA")
        # agora preciso retirar o elemento das duas listas e criar uma nova
        
    else:
        print("Deu errado a logica, refazer !")
elif choice_portfolio_rent_return == 2:
    print("Foi escolhido devolver o carro")



# fazer uma lista de carros
"""
Escolha qual carro quer alugar, com um codigo
Escolha por quantos dias deseja alugar
confirmar ou nao o aluguel do carro, colocando o preço total na mensagem
apos isso, opcao do que deseja fazer : mostrar portfolio, alugar um carro ou devolver um carro
caso seja devolver, deve aparecer uma lista igual na escolha, porém com o item em outra lista 
"""


