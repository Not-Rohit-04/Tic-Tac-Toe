def game_board(board,player):
    print("\n")
    print(f'Current-Player:- {player}')
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def check_for_winner(board, player):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_full(board):
    for space in board:
        if space in ['1','2','3','4','5','6','7','8','9']:
            return False
    return True

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'X'
    
    print('Welcome to tic tac toe')
    game_board(board,current_player)
    
    while True:
        try:
            choice = input(f'Player {current_player} ; choose a position(1-9)').strip()
            position = int(choice)-1
            
            if position < 0 or position > 8 :
                print('Enter a valid position between(1-9).')
                continue
            
            if board[position] in ['X','O']:
                print('Position is already taken, choose another position(1-9)')
                continue
                
            board[position]=current_player
            game_board(board,current_player)
            
            if check_for_winner(board,current_player):
                print(f'Player {current_player} wins, welldone.🎆🎆🎆🎆')
                break
        
            if is_full(board):
                print("\nIt's a Draw.")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print("Please input a valid whole number between 1 and 9.")
            
            
if __name__ == '__main__':
    play_game()