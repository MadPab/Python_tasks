import random

'''На доработке. Не готово'''

def empty_board(board):
    for i in range(3):
        print(board[i * 3], board[1 + i * 3], board[2 + i * 3])


def get_available_cells(board):
    return [cell for cell in board if cell != 'X' and cell != 'O']


def tic_tac_toe(board):
    choice = input('Хотите за крестики или нолики? (X/O): ')
    if choice.lower() == 'x':
        while True:
            empty_board(board)
            cell = int(input('Введите номер ячейки: '))
            print(f'Человек поставил крестик на ячейку {cell}')
            if cell in get_available_cells(board):
                board[cell - 1] = 'X'
                empty_board(board)

                end_game = input('Это конец игры? (Y/N): ')
                if end_game.lower() == 'y':
                    print('Игра окончена')
                    break
                empty_board(board)

                available_cells = get_available_cells(board)
                if available_cells:
                    comp = min(available_cells)
                    board[int(comp) - 1] = 'O'
                    print(f'Компьютер поставил нолик на ячейку {comp}')
                else:
                    print('Нет свободных ячеек!')

            else:
                print('Введите другое число')
    elif choice.lower() == 'o':
        while True:
            empty_board(board)
            cell = int(input('Введите номер ячейки: '))
            print(f'Человек поставил нолик на ячейку {cell}')
            if cell in get_available_cells(board):
                board[cell - 1] = 'O'
                empty_board(board)

                end_game = input('Это конец игры? (Y/N): ')
                if end_game.lower() == 'y':
                    print('Игра окончена')
                    break
                empty_board(board)

                available_cells = get_available_cells(board)
                if available_cells:
                    comp = min(available_cells)
                    board[int(comp) - 1] = 'X'
                    print(f'Компьютер поставил крестик на ячейку {comp}')
                else:
                    print('Нет свободных ячеек!')

            else:
                print('Введите другое число')

board = list(range(1, 10))
tic_tac_toe(board)