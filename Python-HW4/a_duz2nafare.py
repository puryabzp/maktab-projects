fields = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
fields_key = []
for key in fields:
    fields_key.append(key)
def printfield(field):
    print(field['7'] + '|' + field['8'] + '|' + field['9'])
    print('=====')
    print(field['4'] + '|' + field['5'] + '|' + field['6'])
    print('=====')
    print(field['1'] + '|' + field['2'] + '|' + field['3'])
# main function
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printfield(fields)
        print("turn " + turn + ".Move to which place?")

        move = input()

        if fields[move] == ' ':
            fields[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if fields['7'] == fields['8'] == fields['9'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['4'] == fields['5'] == fields['6'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['1'] == fields['2'] == fields['3'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['1'] == fields['4'] == fields['7'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['2'] == fields['5'] == fields['8'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['3'] == fields['6'] == fields['9'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['7'] == fields['5'] == fields['3'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break
            elif fields['1'] == fields['5'] == fields['9'] != ' ':
                printfield(fields)
                print("\nGame Over.\n")
                print(turn + " won")
                break

                # equality between X and O turn
        if count == 9:
            print("\nGame Over.\n")
            print("equalityy between X and O player!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
if __name__ == "__main__":
    game()