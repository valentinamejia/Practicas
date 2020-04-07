def display_winner(player):
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + " wins!")


def check_row_winner(x):
    """
    Return the player number that wins for that row.
    If there is no winner, return 0.
    """
    if x.count(x[0]) == len(x) and x[0] != 0:
        return x[0]
    else:
        return 0


def get_col(game, col_number):
    return [game[x][col_number] for x in range(size)]


def get_row(game, row_number):
    return game[row_number]


def get_diag(game):
    return [game[row_num][col] for row_num, col in enumerate(reversed(range(size)))]


def get_down_diag(game):
    return [game[x][x] for x in range(size)]


def check_winner(game):
    game_slices = []
    for index in range(size):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))
    game_slices.append(get_diag(game))
    game_slices.append(get_down_diag(game))

    for game_slice in game_slices:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return winner


def start_game():
    return [[0 for i in range(size)] for i in range(size)]


def check_available(game, row, column):
    if game[row][column] != 0:
        print('This position is occupated, choose another')
        return False
    else:
        return True


def display_game(game, player= 0, row=0, column=0):
    print('   ' + ' '.join([str(i) for i in range(size)]))
    d = {2: "O", 1: "X", 0: "_"}
    game[row][column] = player
    for row_num in range(size):
        new_row = []
        for col_num in range(size):
            new_row.append(d[game[row_num][col_num]])
        print(row_num, "|" + "|".join(new_row) + "|")


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def moves_exist(game):
    for row_num in range(size):
        for col_num in range(size):
            if game[row_num][col_num] == 0:
                return True
    return False


if __name__ == '__main__':
    start = True
    try:
        while start:
            size = int(input('What size do you want the board to be? : '))
            player = 1
            available = True
            winner = 0
            game = start_game()
            display_game(game)
            while winner == 0 and moves_exist(game):
                print("Currently player: " + str(player))
                row = (int(input("Which row? ")))
                column = (int(input("Which column?  ")))
                available = check_available(game, row, column)
                while available:
                    display_game(game, player, row, column)
                    available = False
                    player = switch_player(player)
                winner = check_winner(game)
            display_winner(winner)
            again = input('the game is over, would you like to play again? (y/n) : ')
            if again.lower() == 'y':
                print('restarting')
            elif again.lower() == 'n':
                print('Goodbye')
                break
            else:
                print('invalid input')
                break

    except Exception as e:
        print('Burroooo', e)
