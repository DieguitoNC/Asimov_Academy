"""
Determinar como que é feito para vencer


"""

class Tic_Tac_Toe:
    
    
    def __init__(self):
        self.game = [1,2,3,4,5,6,7,8,9]
        self.user = []
        self.computer = []
    
    def possibilitys_to_win(self):
        if [1,2,3] in self.game:
            return scoreboard + 1
        elif [1,4,7] in self.game:
            return scoreboard + 1
        elif [7,8,9] in self.game:
            return scoreboard + 1
        elif [3,6,9] in self.game:
            return scoreboard + 1
        elif [1,5,9] in self.game:
            return scoreboard + 1
        elif [3,5,7] in self.game:
            return scoreboard + 1
        elif [2,5,8] in self.game:
            return scoreboard + 1
        elif [4,5,6] in self.game:
            return scoreboard + 1
        elif [7,8,9] in self.game:
            return scoreboard + 1
        #aqui sao todas as opcoes de vitoria
        
    
    def run_game(self):
        continue_const = 0
        while continue_const == 0:
            print("================================")
            print("Bem-vindo ao jogo da velha")
            print("================================")
            print()
            print("Faça sua jogada !")
            print("[1,2,3]")
            print("[4,5,6]")
            print("[7,8,9]")
            player_choice = input()
            self.user.append(player_choice)
            continue_const=+1


Tic_Tac_Toe.run_game()