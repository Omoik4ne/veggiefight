from veggiefight import Ring, KillerTomato, PuncherBroccoli, BrawlerCarrot

t1 = KillerTomato()
b1 = PuncherBroccoli()
c1 = BrawlerCarrot()

# c1.hp = 7
# print(c1.hp)
# c1.attack

score = {t1: 0, b1: 0, c1:0}

fights = [
    (t1,b1),(b1,t1)
    (b1,c1),(c1,b1)
    (c1,t1),(t1,c1)
]

for fighters in fights:
    ring = Ring(fighters[0], fighters[1])

    winner = None

    while winner is None:
        winner = ring.round_fight()

    score[winner] += 1

print(score)

