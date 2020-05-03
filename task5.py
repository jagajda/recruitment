import sys
import random
class Game:
    def __init__(self, game_id=0, games=0):
        self._id = game_id
        self._games = games
        self._players = []
        self._rolls = []

    def add_roll(self, roll):
        self._rolls.append(roll)

    def add_player(self, player):
        self._players.append(player)

    def print_summary(self, mode):
        print("TOTAL NUMBER OF PLAYERS: ", len(self._players))
        print("TOTAL NUMBER OF GAMES: ", self._games)
        if mode == 1:
            print("\nRESULTS")
            print("GAME    WIN NUMBER")
            for i in self._rolls:
                i.print_summary(mode)
            print("PLAYER  BET            WIN           LOSE")
            for j in self._players:
                j.print_summary(mode)
        elif mode == 2:
            for j in self._rolls:
                j.print_summary(mode)

    def get_players(self):
        return self._players
    
    def update_results(self):
        for i in self._players:
            i.update_results

class Roll:
    def __init__(self, roll_id=0, result=None):
        self._id = roll_id
        if result is None:
            self._result = random.randint(1,50)
        else:
            self._result = result
        self._winners = []
        self._bets = []

    def get_id(self):
        return self._id

    def set_winners(self, players_list, mode):
        for i in players_list:
            if mode == 1: 
                for j in i._bets.values():
                    if j == self._result:
                        self._winners.append(i)
                        i.add_win(self)
                    else:
                        i.add_lost(self)
                i.update_results()
                        
            elif mode == 2:
                for key, value in i._bets.items():
                    if key == self._id: 
                        if value == self._result:
                            self._winners.append(i)
                            i._rolls_won.append(self)
                        else:
                            i._rolls_lost.append(self)
    
    def update_bets(self, player_list):
        for i in player_list:
            for key, value in i.get_bets().items():
                if key == self._id:
                    self._bets.append(value)

    def print_summary(self,mode):
        if mode == 1:
            print("{:6}{:10}".format(self._id, self._result))

        elif mode == 2:
            print("GAME NUMBER: ", self._id)
            bets = ', '.join([str(i) for i in self._bets])
            print("BET NUMBERS: ", bets)
            print("WIN NUMBER: ", self._result)
            winners = ', '.join([str(i.get_name()) for i in self._winners])
            if len(self._winners) == 0:
                winners = "None"
            print("WINNERS: ", winners)
            print("\n")

class Player:
    def __init__(self, player_id=0,  name=''):
        self._player_id = player_id
        self._name = name
        self._bets = {}
        self._rolls_won = []
        self._rolls_lost = []

    def get_name(self):
        return self._name

    def add_win(self, roll):
        self._rolls_won.append(roll)

    def add_lost(self, roll):
        self._rolls_lost.append(roll)

    def get_bets(self):
        return self._bets

    def get_bets_from_input(self, input_string='', bet_no=None):
        if bet_no is not None:
            self._bets.update({bet_no : int(input_string)})
        else:
            index = 1
            for i in input_string.split(','):
                self._bets.update({index : int(i)})
                index += 1

    def print_summary(self, mode):
        out = ""
        bets = ", ".join([str(value) for value in self._bets.values()])
        wins = ", ".join([str(i.get_id()) for i in self._rolls_won])
        if len(self._rolls_won) == 0:
            wins = "None"
        losses = ", ".join([str(i.get_id()) for i in self._rolls_lost])
        if mode == 1:
            out += "{:<10}".format(self._name)
            out += "{:13}".format(bets)
            out += "{:13}".format(wins)
            out += "{:14}".format(losses)
            print(out)
        else:
            pass

    def update_results(self):
        self._rolls_won = list(set(self._rolls_won))
        self._rolls_lost = list(set(self._rolls_lost))      

def main():
    if len(sys.argv) < 4:
        sys.exit("Too few arguments")
    elif len(sys.argv) == 4:
        players = int(sys.argv[1])
        games = int(sys.argv[2])
        mode = int(sys.argv[3])
    else:
        sys.exit("Incorrect number of arguments")
    if mode not in(1,2):
        sys.exit("Incorrect game mode")
    if mode == 1:
        game = Game(1, games)
        for i in range(1, players + 1):
            name = input("Enter name for player no {}: ".format(i))
            bets = input("Type player bets for every game separated by comma \",\" (values smaller than 50): ")
            while len(bets.split(',')) != games:
                bets = input("Incorrect number of bets, the number of bets must be equal to {}, enter bets once again: ". format(games))
            player = Player(i, name)
            player.get_bets_from_input(bets)
            game.add_player(player)    
        for i in range(1,games + 1):
            roll = Roll(i)
            roll.set_winners(game.get_players(), mode)
            roll.update_bets(game.get_players())
            game.add_roll(roll)
        game.print_summary(mode)
    elif mode == 2:
        player_list = []
        for i in range(1, players + 1):
            name = input("Enter name for player no {}: ".format(i))
            player_list.append(Player(i, name))
        for i in range(1, games + 1):
            game = Game(i, games)
            print("Round {}". format(i))
            for j in player_list:
                bets = input("Type bet for player {}: ".format(j.get_name()))
                j.get_bets_from_input(bets, i)
                print(bets)
                game.add_player(j)
            roll = Roll(i)
            roll.set_winners(game.get_players(), mode)
            roll.update_bets(game.get_players())
            game.add_roll(roll)
            game.print_summary(mode)

if __name__ == "__main__":
    main()
