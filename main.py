# WELCOME


class Points_tracker:

    HIGHEST = True
    LOWEST = False
    #TODO zmena nazvu

    def __init__(self):
        self.players: dict[str, int] = {}
        # Initial mode is max
        self.mode: bool = self.HIGHEST

        self.round = 1

    def set_mode(self):
        mode_input = input("Is the goal to have lowest or highest score? (Enter H/L) ").lower()

        while mode_input != "h" and mode_input != "l":
            mode_input = input("Invalid input. Try again. (Enter H/L) ").lower()

        if mode_input == "l":
            self.mode = self.LOWEST
        else:
            self.mode = self.HIGHEST

    def set_players(self):
        print("Enter names of the players. When finished, enter \"submit\".")
        while True:
            name = input(f"Name of player {len(self.players) + 1}: ").strip()

            if name.lower() == "submit":
                if not self.players:
                    print("You need to enter at least one player!")
                    continue
                break

            if name in self.players:
                print("Player with this name already exists.")
                continue

            if name:
                self.players[name] = 0

    def play_round(self) -> bool:
        print("\nRound ", self.round, ":")

        for player in self.players:
            new_score = input("Points for " + player +  ": ")
            self.players[player] += int(new_score)
        
        print("\nResults after ", self.round, ". round:\n")

        for player, score in self.players.items():
            print(player, ": ", score)

        self.round += 1
        
        next_round = input("Do you want to continue? (Y/N)").upper()
        while next_round != "Y" and next_round != "N":
            next_round = input("Invalid input. Please enter Y/N.").upper()
        return next_round == "Y"

    def show_results(self):
        print("\nFinal results after", self.round - 1, "rounds:")

        winner_score = 0
        place = 0
        
        # TODO special case for players with same number of points - currently sorted in order of iteration 
        last_score: int | None = None

        while self.players:
            if self.mode == self.LOWEST:
                winner_score = min(self.players.values())
            else:
                winner_score = max(self.players.values())

            if not last_score or last_score != winner_score:
                place += 1
                
        
            for player, score in self.players.items():
                if score == winner_score:
                    print(place, ". ", player, " with ", winner_score, " points.")
                    last_score = winner_score

                    self.players.pop(player)
                    break
        print("Congrats!")
        
    
def main():
    print("Welcome!")
    
    game = Points_tracker()
    game.set_mode()
    game.set_players()

    print("Each round, you will be asked to add points to each player.")
    print("\nReady to play?")

    while True:
        if not game.play_round():
            break

    game.show_results()
    

if __name__ == "__main__":
    main()
