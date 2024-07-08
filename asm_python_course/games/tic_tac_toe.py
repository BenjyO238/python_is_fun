matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

playerOne = 1
playerTwo = 2

def print_matrix():
    for i in range(3):
        for j in range(3):
            current = " "
            if matrix[i][j] == playerOne:
                current = "X"
            elif matrix[i][j] == playerTwo:
                current = "O"
            print(f" {current} ", end="")
            if j < 2:
                print(" -", end="")
        print("")
        if i < 2:
            print("----+----+----")
    print()

def validate_input(x, y):
    if x >= 3 or y >= 3 or x < 0 or y < 0:
        print("\nOut of bound! Enter again...\n")
        return False
    elif matrix[x][y] != 0:
        print("\nAlready entered! Try again...\n")
        return False
    return True

def get_input(currentPlayer):
    if currentPlayer == playerOne:
        print("\nPlayer One's Turn")
    else:
        print("\nPlayer Two's Turn")
    failed = True
    while failed:
        try:
            x = int(input("Enter the x coordinate (0-2): "))
            y = int(input("Enter the y coordinate (0-2): "))
            if validate_input(x, y):
                matrix[x][y] = currentPlayer
                failed = False
                print_matrix()
        except ValueError:
            print("Error occurred! Enter valid integers between 0 and 2.")

def check_rows():
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return row[0]
    return 0

def check_columns():
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != 0:
            return matrix[0][col]
    return 0

def check_diagonals():
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != 0:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != 0:
        return matrix[0][2]
    return 0

def check_winner():
    result = check_rows()
    if result == 0:
        result = check_columns()
    if result == 0:
        result = check_diagonals()
    return result

def main():
    result = 0
    i = 0
    while result == 0 and i < 9:
        if i % 2 == 0:
            get_input(playerOne)
        else:
            get_input(playerTwo)
        result = check_winner()
        i += 1

    if result == 1:
        print("Player One is the winner")
    elif result == 2:
        print("Player Two is the winner")
    else:
        print("Draw")

main()
