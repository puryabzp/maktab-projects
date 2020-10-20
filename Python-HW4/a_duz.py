def print_state(array):
    print("#" * 40)
    print()
    for i in range(len(array)):
        print("=" * 30)
        for j in range(len(array)):
            print("  |  ", end=" ", sep=" ")
            print(array[i][j], end=" ", sep=" ")
        print()


def get_input(array):
    while True:
        x = input(">>> enter row and column with space in range [0, 2], like: ")
        row, col = [int(i) for i in x.split(' ')]
        if array[row][col] == 0:
            array[row][col] = 'X'
            break
        else:
            print('This element is full, enter another row and columns')

    print_state(array)
    return array


def wise_player(array):
    print_state(array)

    if array[1][1] == 0:
        array[1][1] = 'O'
        print_state(array)
        return array

    winning_states = [
        [[0, 0], [0, 1], [0, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
        [[0, 2], [1, 2], [2, 2]]
    ]

    input_row, input_col = -1, -1
    for row in winning_states:
        count_X = 0
        for element in row:
            row, col = element
            if array[row][col] == 'X':
                count_X += 1
            elif array[row][col] == 0:
                input_row, input_col = row, col

        if count_X == 2:
            array[input_row][input_col] = 'O'
            print_state(array)
            return array

    if input_row != -1 and input_col != -1:
        array[input_row][input_col] = 'O'
        print_state(array)
        return array
    else:
        print_state(array)
        print('The board is full')
        return array


def check_winner(array, player):
    winning_states = [
        [[0, 0], [0, 1], [0, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
        [[0, 2], [1, 2], [2, 2]]
    ]

    for row in winning_states:
        count = 0
        for element in row:
            row, col = element
            if array[row][col] == 'X':
                count += 1

        if count == 3:
            return True
    return False


array = [['X', 0, 0], [0, 'X', 0], [0, 0, 'X']]
# get_input(array)

# wise_player(array)
# print(check_winner(array, 'X'))

if __name__ == '__main__':
    array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    edame = True
    while (edame):
        print_state(array)
        get_input(array)
        win = check_winner(array, 'X')
        if not win:
            wise_player(array)
            win = check_winner(array, 'O')
        if win:
            edame = False