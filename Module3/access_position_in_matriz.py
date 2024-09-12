piece = 0
board = []

for i in range(8):
    row = [piece for i in range(8)]
    board.append(row)

# How to acess on x position ?
board[0][0] = 1 # Atribuindo o valor 1 na linha 0 e coluna 0

for row in board:
    print(row)

# No sentido de acesso, vertical é o número da linha
# Horizontal é o número da coluna
# O primeiro [0] é a vertical, número da linha
# O segundo [0] é a horizontal, número da coluna