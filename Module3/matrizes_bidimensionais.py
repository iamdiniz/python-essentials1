piece = 0
board = []

for i in range(8):
    row = [piece for i in range(8)]
    board.append(row)

for row in board:
    print(row)