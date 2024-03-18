board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    '''Prints the Tic-Tac-Toe board'''
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_win(player):
    '''Checks rows, columns, and diagonals for win condition for a given player
    
    Parameters:
    - player: str - The player ('X' or 'O') to check for win
    
    Returns:
    - bool: True if the player wins, False otherwise
    '''
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Fixed: Changed 'not all' to 'all'
            return True
        if all([board[j][i] == player for j in range(3)]):  # Fixed: Changed 'not all' to 'all'
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:  # Fixed: Changed 'board[1][0]' to 'board[0][0]'
        return True
    return False  # Fixed: Added explicit return False if no win condition is met

def tally_wins(results):
    '''Tally the number of wins from a list of results
    
    Parameters:
    - results: list - List of boolean results indicating win (True) or loss (False)
    
    Returns:
    - int: Total number of wins
    '''
    return sum(results)

def main():
    '''Main function to control the Tic-Tac-Toe game'''
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(current_player)
                results.append(win)
                if win:
                    print_board()
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print("Invalid input! Please enter row and column values within the range (0-2).")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")

if __name__ == "__main__":
    main()
