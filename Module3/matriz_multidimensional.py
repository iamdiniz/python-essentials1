# matriz multidimensional (mais de duas dimensões)

# Cubo - uma matriz tridimensional (3x3x3)
 
cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
for row in cube:
    print(row)
    
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'