
import time
import random

from .enemy import Enemy



class Player:
    nameP = ""
    classP = ""
    hpP = 0
    endurance = 0
    mana = 0
    weapon = ""
    armor = None
    damage= 0
    def __init__(self, newNameP, newClassP, newHpP, newEnduranceP, newManaP,newDamageP, newWeaponP="нема оружия", newArmorP="нема брони"):
        self.namep = newNameP
        self.classp = newClassP
        self.hp = newHpP
        self.endurance = newEnduranceP
        self.mana = newManaP
        self.weapon = newWeaponP
        self.armor = newArmorP
        self.damage = newDamageP

    def print_infoP(self):
        print(f"Имя игрока: {self.namep}\nКласс: {self.classp}\nХп: {self.hp}\nВыносливость: {self.endurance}\nОружие: {self.weapon}\nБронь: {self.armor}\n дамаг: {self.damage}")
    def say(self,text):
        print(f"Игрок {self.namep} говорит: '{text}'")

    def choose_action(self,enemy:Enemy):
        choose = input("Выбор действия 1. Атаковать  2. Защититься  3. Уклониться   4. Бежать")
        if choose == "1":
            enemy.ehp =  enemy.ehp - self.damage
            print("Игрок {self.name} наносит {self.damage} урона")
        elif choose == "2":
            self.hp = self.hp - enemy.edamage / 3
            print("Игрок {enemy.ename} защитился")
        elif choose == "3":
            print("Игрок {enemy.ename} уклонился")
        elif choose == "4":
            print("Игрок {enemy.ename} просто убежал XD")

        
    def fight(self,enemy:Enemy):
        print(f"Игрок {self.namep} вступил в схватку {enemy.ename}")
        while True:
            if self.hp <= 0:
                print("\nУМЕр")
                break
            elif enemy.ehp <= 0:
                print("ххихаха, умер")
                break

            self.choose_action(enemy)

            print("Игрок {self.name} наносит {self.damage} урона")
            print("Игрок {enemy.ename} наносит {enemy.edamage} урона")
            self.hp -= enemy.edamage
            enemy.ehp -= self.damage
            print(f"У {self.namep} осталось {self.hp} здоровья")
            print(f"У {enemy.ename} осталось {enemy.ehp} здоровья")
            time.sleep(0.5)


# player1.say("блин...*cry*")
