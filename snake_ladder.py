import random

# Function to move the pawn and check for winning or landing on snakes or ladders
def Move(Player, value):
    """This function moves the pawn and also checks for winning and overflow."""
    snake_squares = {16: 4, 22: 10, 33: 20, 48: 24, 62: 56, 78: 69, 74: 60, 91: 42, 97: 6}
    ladder_squares = {3: 12, 7: 23, 11: 25, 21: 56, 47: 53, 60: 72, 80: 96}
    Throw = random.randint(1, 6)
    num = value + Throw
    if num > 100:
        print("BAD LUCK, YOU CAN'T MOVE, YOU NEED A {} TO WIN".format(100 - value))
        return value
    if num == 100:
        return num

    # Print the result of the move
    print(Player, "rolled a", Throw, "and is now on", num)
    if num in snake_squares:
        print(Player, "got bitten by a snake and is now on square", snake_squares[num])
        num = snake_squares[num]
    elif num in ladder_squares:
        print(Player, "climbed a ladder and is now on square", ladder_squares[num])
        num = ladder_squares[num]

    return num

# Function to get the number of players
def playerscount():
    """Accepts the number of players."""
    while True:
        try:
            numofplayers = int(input("How many players are in the game? "))
            if 2 <= numofplayers <= 4:
                return numofplayers
            else:
                print("Number of players must be between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Function to get player names
def nameofplayers(N):
    """Accepts the names of players and returns the list of names."""
    Names = []
    for i in range(N):
        Names.append(input("What is the name of Player " + str(i + 1) + "? "))
    return Names

# Function for each player's turn
def turn(player, pos):
    COMMANDSTATE = "Press Enter to continue or press 'stop' to stop: "
    WINSTATEMENT = "wins the game! Congratulations!"
    Command = input(f"Hey {player}! It's your turn now. {COMMANDSTATE}")
    
    if Command.lower() == 'stop':
        # If the user commands to stop, the game stops
        return True, pos
    
    pos = Move(player, pos)
    if pos == 100:
        print(player, WINSTATEMENT)
        return True, pos
    
    return False, pos

# Main function to run the game
def main():
    """The main function."""
    numofplayers = playerscount()
    playernames = nameofplayers(numofplayers)
    print(", ".join(playernames), "- Welcome To Snakes And Ladders")

    PosArr = [1] * numofplayers  # Positions of players' pawns
    GameOver = False  # Flag to check if the game should continue
    TURNS = 0  # Track turns
    
    while not GameOver:      
        while TURNS < numofplayers:
            # Each player's move in sequence
            GameOver, PosArr[TURNS] = turn(playernames[TURNS], PosArr[TURNS])
            if GameOver:
                return
            TURNS += 1
        TURNS = 0

if __name__ == '__main__':
    main()
