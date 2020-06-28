def print_board(cells):
    print("---------")
    print("| {} {} {} |".format(cells[2],cells[5],cells[8]))
    print("| {} {} {} |".format(cells[1],cells[4],cells[7]))
    print("| {} {} {} |".format(cells[0],cells[3],cells[6]))                        
    print("---------")

def input_coord(cells):
    right_coord = [1,2,3]
    coordinate_x, coordinate_y = 0, 0
    coordinates = [coordinate_x, coordinate_y]
    while coordinates not in board or cells[board.index(coordinates)] != " ":
        try:
            coordinate_x, coordinate_y =input("Enter the coordinates:").split()
            if coordinate_x not in right_coord or coordinate_y not in right_coord:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")
        else:
            coordinates = [int(coordinate_x), int(coordinate_y)]
            if coordinates in board and cells[board.index(coordinates)] != " ":
                print("This cell is occupied! Choose another one!")        
    return coordinates
    
board = [[1, 3], [2, 3], [3, 3], 
         [1, 2], [2, 2], [3, 2], 
         [1, 1], [2, 1], [3, 1]]

cells = [" " for item in range(9)]

x_win = ["X", "X", "X"]
o_win = ["O", "O", "O"]
win = [cells[0:3], cells[3:6], cells[6:9], cells[0::3],
    cells[1::3], cells[2::3], cells[0::4], cells[2:7:2]]         
print_board(cells)
move = 0
place = 1

while move < 9 or x_win not in win or o_win not in win:
    coordinates = input_coord(cells)
    if place % 2 == 1:
        cells[board.index(coordinates)] = "X"
    else:
        cells[board.index(coordinates)] = "O"
    win = [cells[0:3], cells[3:6], cells[6:9], cells[0::3],
    cells[1::3], cells[2::3], cells[0::4], cells[2:7:2]]
    print_board(cells)
    place += 1    
    move += 1
    print(win)
    if x_win in win:
        print("X wins")
        break
    elif o_win in win:
        print("O wins")
        break
    elif move == 9 and (x_win not in win or o_win not in win):
        print("Draw")
        break
