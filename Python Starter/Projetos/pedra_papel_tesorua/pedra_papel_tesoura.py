#%%
import random



def possible_plays(number):
    if number >= 0 and number < len(plays):
        return plays[number]
    else:
        print("Escolha uma jogada válida entre 0,1 e 2")

def who_wins_the_game(int_chosen_move, computer_number):
    #papel
    if int_chosen_move == 0 and computer_number == 1:
        #papel vs pedra
        print("Você venceu")
        return player_scoreboard + 1
    elif int_chosen_move == 0 and computer_number == 2:
        #Papel vs tesoura
        print("Você perdeu")
        return computer_scoreboard + 1
    elif int_chosen_move == computer_number:
        print("Empatou !")
    elif int_chosen_move == 1 and computer_number == 0:
        #Pedra vs papel
        print("Você Perdeu !")
        return computer_scoreboard + 1
    elif int_chosen_move == 1 and computer_number == 2:
        #Pedra vs Tesoura
        print("Você venceu !")
        return player_scoreboard + 1
    elif int_chosen_move == 2 and computer_number == 0:
        #tesoura vs papel
        print("Você ganhou !")
        return player_scoreboard + 1
    elif int_chosen_move == 2 and computer_number == 1:
        #tesoura vs pedra
        print("Você perdeu !")
        return computer_scoreboard + 1

const = 0

plays = ["Papel", "Pedra", "Tesoura"]
player_scoreboard = 0
computer_scoreboard = 0

print("===============================================")
print("Bem vindo ao jogo de Papel, pedra ou tesouro")
print("===============================================")
print()
print()
    
while const <= 0:
    
    player_scoreboard = 0
    computer_scoreboard = 0
    
    print("Escolha seu lance:")
    print("0 - Papel | 1 - Pedra | 2 - Tesoura")
    
    computer_number = random.randrange(3)
    chosen_move = input()
    print(chosen_move)
    print()
    print("=======================")
    
    try:
        
        int_chosen_move = int(chosen_move)
        my_choice = possible_plays(int_chosen_move)
        print("Sua jogada: {}" .format(my_choice.upper()))
        computer_choice = possible_plays(computer_number)
        print("Jogada do computador: {}" .format(computer_choice.upper()))
        who_wins_the_game(int_chosen_move, computer_number)
    except Exception as e:
        print("O erro foi: {}".format(e))

    
    
    
    
    const_play_again = 0
    while const_play_again == 0:
        print("=======================")
        print()
        print("Jogar novamente ? 0 - SIM | 1 - NÃO")
        play_again = input()
    
        try:
            int_play_again = int(play_again)
            if int_play_again == 0:
                print("Pontuação do comuputador é".format(computer_scoreboard))
                print("Sua pontuação é ".format(player_scoreboard))
                print(player_scoreboard)
                const_play_again = 1
            elif int_play_again == 1:
                const =+1
                const_play_again = 1
            else:
                print("Insira um valor válido")
                            
        except Exception as e:
            print("O erro foi: {}".format(e))

#%%




