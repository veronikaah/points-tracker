# WELCOME

print("Welcome!")

mode_input = input("Is the goal to have minimum or maximum points? (Enter min/max) ")
if mode_input == "min":
    mode = True
else:
    mode = False



print("Secondly, you will enter names of the players. Once you are finished, enter \"submit\" instead.")
print("Each round, you will be asked to add number of points to each player.")
print("If you want to finish the game, enter \"finish\" and you will be shown the results.")

player_count = 0
player_names = []
player_points = []

while True:
    name = input("Name of " + str(player_count + 1) + ". player? ")

    if name == "submit":
        break

    player_names.append(name)
    player_points.append(0)
    player_count += 1

print()
print("Ready to play?")
print()

round_count = 1


def round(count, points, names) -> bool:
    print()
    print("Round ", count, ":")
    
    for player in range(len(names)):
        inpt = input("Points for " + str(names[player]) +  ": ")

        if inpt == "finish":
            return False
        
        points[player] += int(inpt)

    print()
    print("Results after ", count, ". round:")
    print()

    for player in range(len(names)):
        print(names[player], ": ", points[player])

    return True



while True:
    r = round(round_count, player_points, player_names)
    if not r:
        break
    round_count += 1
    
    


print()
print("Final results:")


results = {}
for i in range(len(player_names)):
    results[player_points[i]] = player_names[i]


place = 1


while results:
    if mode:
        m = min(results.keys())
    else:
        m = max(results.keys())
    print(place, ". ", results[m], " with ", m, " points.")

    results.pop(m)
    place += 1

print("Congrats!")
