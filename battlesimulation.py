import sys




# Everytime a move repeats, chance of combo is over
combo = {}
counter = { 'R': 'S', 'B': 'K', 'L': 'H' }
monster_moves = sys.stdin.readline()
mech_moves = [] 
move_batch = []

for move in monster_moves:
    if move not in combo: # move is different from last
        combo[move] = True
        if len(combo) >= 3: # combo detected
            move_batch = []
            mech_moves.append('C')
        else: # combo is on the way to happening
            move_batch.append(move)
    else: # combo definitely not happening
        combo = { move: True }
        