#%%
const = 0

possible_plays = ["Papel", "Pedra", "Tesoura"]

def possible_plays(number):
    if number == 0:
        paper = possible_plays[0]
        return paper
    elif number == 1:
        rock = possible_plays[1]
        return rock
    elif number == 2:
        scissors = possible_plays[2]
        return scissors
    else:
        print("Escolha uma jogada válida entre 0,1 e 2")


while const <=0:
    print("===============================================")
    print("Bem vindo ao jogo de Papel, pedra ou tesouro")
    print("===============================================")
    
    
    
    
    #my_scoreboard = x
    #computer_scoreboard = x
    print("Escolha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")
    
    chosen_move = input()
    
    try:
        
        int_chosen_move = int(chosen_move)
        my_choice = possible_plays(int_chosen_move)
        print(my_choice)
    except Exception as e:
        print("O erro foi: {}".format(e))
    

    
     
    const=+1

#%%




