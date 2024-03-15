import random


def jogo():
    vida_j = 100
    vida_m = random.randint(60, 80)
    dano_j = random.randint(10, 20)
    dano_m = random.randint(20, 30)
    defesa_j = random.randint(1, 5)
    rodada = 1
    while vida_j > 0 and vida_m > 0:
        print("Aventureiro: vida %d - att - %d - def %d" % (vida_j, dano_j, defesa_j))
        print("Monstro: vida %d - att - %d" % (vida_m, dano_m))
        print("Rodada %d" % rodada)
        vida_m = vida_m - (random.randint(1, dano_j))
        if vida_m < 0:
            break
        atk = random.randint(1, dano_j) - defesa_j
        if atk > defesa_j:
            vida_j = vida_j - atk
        rodada += 1
    if vida_j < 0:
        print("Você morreu.")
    else:
        print("O Monstro morreu.")


jogo()
