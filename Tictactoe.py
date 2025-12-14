board = {'7':' ', '8':' ', '9':' ', '4':' ', '5':' ', '6':' ', '1':' ', '2':' ', '3':' '}
def printboard(board):
    print(board['7']+' '+ board['8']+' ' + board['9'])
    print('-+-+-')
    print(board['4']+' '+ board['5']+' ' + board['6'])
    print('-+-+-')
    print(board['1']+' '+ board['2']+' ' + board['3'])
def game():
    turn = 'x'
    count = 0
    for i in range(10):
        printboard(board)
        print("It is your turn now" + turn + "Which place would you like to move too?")
        move = input()
        if board[move] == ' ':
            board[move] = turn
            count+=1
        else:
            print("That place is already filled out.\nMove to which place?")
            continue
        if count>=4:
            if board['7'] == board['8'] == board['9'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['7'] == board['4'] == board['1'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['8'] == board['5'] == board['2'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['9'] == board['6'] == board['3'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
            elif board['9'] == board['5'] == board['1'] != ' ':
                printboard(board)
                print("\nGame Over!\n")
                print('*****'+'*****')
                break
        if count == 9:
            print("\nGame Over\n")
            print("It is a tie!")
        if turn == 'x':
            turn = 'O'
        else:
            turn = 'x'
    restart = input("Do you want to play again?(y/n): ")
    if restart == 'y' or restart == 'Y':
        for key in board:
            board[key] = ' '
    game()
if __name__ == "__main__":
    game()