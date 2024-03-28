moves = input().strip()
cups = [1, 0, 0]
def A(): global cups; cups = [cups[1]] + [cups[0]] + [cups[2]]
def B(): global cups; cups = [cups[0]] + [cups[2]] + [cups[1]]
def C(): global cups; cups = [cups[2]] + [cups[1]] + [cups[0]]
for move in moves: exec(f"{move}()")
print(cups.index(1)+1)