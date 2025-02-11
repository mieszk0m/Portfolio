def run(moves, move_descriptions):
    for move in moves:
            for przycisk in move_descriptions: 
                if przycisk[0] == move:
                     print(move + przycisk[1])
f = 'f'
b = 'b'
l = 'l'
r = 'r'
q = 'q'
x = [f, f, r, q]
y = [[f, " Zwierzak idzie do przodu"], [b, " Zwierzak idzie do tyłu"], [l, " Zwierzak skręca w lewo"], [r, " Zwierzak skręca w prawo"]]
run(x, y)