print("Welcome to the Memory Labyrinth Game")

print("Controls:")
print("W = Up")
print("A = Left")
print("S = Down")
print("D = Right")
print()
print("Find the treasure (T)")
print("Avoid traps (X)")
print("You start with 3 health.")
print()
# This is the Base Entity Class


class Entity:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol



# Player Class


class Player(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, "@")
        self.health = 3

    def move(self, direction):

        if direction.lower() == "w" and self.x > 0:
            self.x -= 1

        elif direction.lower() == "s" and self.x < 4:
            self.x += 1

        elif direction.lower() == "a" and self.y > 0:
            self.y -= 1

        elif direction.lower() == "d" and self.y < 4:
            self.y += 1



# Trap Class


class Trap(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, "X")



# Treasure Class


class Treasure(Entity):

    def __init__(self, x, y):
        super().__init__(x, y, "T")



# Grid Renderer


def render_grid(player, treasure, traps):

    for row in range(5):

        for col in range(5):

            symbol = "."

            if row == player.x and col == player.y:
                symbol = player.symbol

            elif row == treasure.x and col == treasure.y:
                symbol = treasure.symbol

            else:
                for trap in traps:
                    if row == trap.x and col == trap.y:
                        symbol = trap.symbol

            print(symbol, end=" ")

        print()

    print(f"\nHealth: {player.health}")
    print()



# Collision Detection


def check_traps(player, traps):

    for trap in traps:

        if player.x == trap.x and player.y == trap.y:

            print("\a")   # sound

            player.health -= 1

            print("BOOO! You stepped on a trap!")
            print("-1 Health")

            traps.remove(trap)
            break

def check_treasure(player, treasure):

    return player.x == treasure.x and player.y == treasure.y



# Main Game


def main():

    player = Player(0, 0)

    treasure = Treasure(4, 4)

    traps = [
        Trap(1, 2),
        Trap(2, 3),
        Trap(3, 1)
    ]

    while True:

        render_grid(player, treasure, traps)

        move = input("Move (W(Up)/A(Left)/S(Down)/D(Right)): ")

        player.move(move)

        check_traps(player, traps)

        if player.health <= 0:
            print("\nGAME OVER!")
            break

        if check_treasure(player, treasure):

            print("\n CHEERS! ")
            print("YOU FOUND THE TREASURE!")
            print("YOU WIN!")

            break


# Run game
main()