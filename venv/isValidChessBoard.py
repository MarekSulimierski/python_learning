import pprint

chessBoard = {'a1': 'A1', 'a2': 'A2', 'a3': 'A3', 'a4': 'A4', 'a5': 'A5', 'a6': 'A6', 'a7': 'A7', 'a8': 'A8',
              'b1': '', 'b2': '', 'b3': '', 'b4': '', 'b5': '', 'b6': '', 'b7': '', 'b8': '',
              'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'c7': '', 'c8': '',}

def validChessboard(board):
    print(board['a1'] + '|' + board['a2'] + '|' + board['a3'] + '|' + board['a4'] + '|' + board['a5'] + '|'+ board['a6'] + '|' + board['a7'] + '|' + board['a8'])
    #print('-------------------------------------------------------------------------------------------------------')
validChessboard(chessBoard)

for i in range (0,7):
    pawnSet = input('Podaj pole na planszy szachowej celem umieszczenia gońca(a1-h8): ')
    if pawnSet in chessBoard:
        chessBoard[pawnSet] = "Pawn"
    elif pawnSet not in chessBoard:
        print("Nieprawidłowa pozycja. Podaj wartość w przedziale (a1:h8)")
validChessboard(chessBoard)
print(chessBoard)
