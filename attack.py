# Crear un juego RPG - secuencia de ataque...

import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh): # Este código se ejecuta al iniciar un objeto de esta clase
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("EL ataque es", self.atkl)

    def getHp(self):
        print("La vida es", self.hp)

enemy1 = Enemy(40, 49)
enemy2 = Enemy(75, 90)

enemy1.getAtk()
enemy1.getHp()

enemy2.getAtk()
enemy2.getHp()


'''

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("El enemigo te da una leche de", dmg, "puntos de daño. Tu vida actual es de", playerhp)

    if playerhp > 30:
        continue # Esto lo que hace es que ignora el resto del loop y vuelve al inicio. Es una alternativa al break

    print("Estás muy mal. Te teletransportas a la posada mas cercana")
    break # Lo que hace es salir del loop

'''