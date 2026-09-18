# WELCOME


class Points_tracker:

    MAX_POINTS = True
    MIN_POINTS = False

    def __init__(self):
        self.players: dict[str, int] = {}
        # Initial mode is max
        self.mode: bool = self.MAX_POINTS

        self.round = 1

    def set_mode(self):
        mode_input = input("Is the goal to have minimum or maximum points? (Enter min/max) ").lower()

        while mode_input != "min" and mode_input != "max":
            mode_input = input("Invalid input. Try again. (Enter min/max) ")
            mode_input = mode_input.lower()

        if mode_input == "min":
            self.mode = self.MIN_POINTS
        else:
            self.mode = self.MAX_POINTS

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
            inpt_points = input("Points for " + player +  ": ")
            self.players[player] += int(inpt_points)
        
        print("\nResults after ", self.round, ". round:\n")

        for player, points in self.players.items():
            print(player, ": ", points)

        self.round += 1
        
        next_round = input("Do you want to continue? (Y/N)").upper()
        while next_round != "Y" and next_round != "N":
            next_round = input("Invalid input. Please enter Y/N.").upper()
        return next_round == "Y"

    def show_results(self):
        print("\nFinal results after", self.round - 1, "rounds:")

        winner_points = 0
        place = 0
        
        # TODO special case for players with same number of points - currently sorted in order of iteration 
        last_points: int | None = None

        while self.players:
            if self.mode == self.MIN_POINTS:
                winner_points = min(self.players.values())
            else:
                winner_points = max(self.players.values())

            if not last_points or last_points != winner_points:
                place += 1
                
        
            for player, points in self.players.items():
                if points == winner_points:
                    print(place, ". ", player, " with ", winner_points, " points.")
                    last_points = winner_points

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
