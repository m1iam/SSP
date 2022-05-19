import random


THINGS = ['Ножиці','Папір','Камінь','Колодязь','Вогонь','Вода']
WATER = ['Папір','Колодязь']
FIRE = ['Вода','Колодязь','Камінь']
SCISSORS = ['Камінь','Вода','Колодязь']
PAPER = ['Вогонь','Ножиці','Вода']
STONE = ['Папір','Вода']
KOLODJAZ = ['Папір','Камінь']
MY_HP = 100
OPPONENT_HP = 100
DAMAGE = 0

#Пропонує на вибір три випадкових елементи
def random_processor():
    first_rand = THINGS[random.randint(0, 1)]
    second_rand = THINGS[random.randint(2, 3)]
    third_rand = THINGS[random.randint(4, 5)]

    start(first_rand, second_rand, third_rand)

def damage_processor(element):
    damage = 0
    if(element == "Вогонь"):
        damage = int(random.randint(25, 35))
    elif(element == "Вода"):
        damage = int(random.randint(5, 10))
    elif(element == "Камінь"):
        damage = int(random.randint(30, 40))
    elif(element == "Папір"):
        damage = int(random.randint(10, 15))
    elif(element == "Колодязь"):
        damage = int(random.randint(35, 45))
    elif(element == "Ножиці"):
        damage = int(random.randint(15, 20))

    return damage

def compare_bolean(element_arr, scnd_el):
    temp = 0
    for x in element_arr:
        if (x == scnd_el):
            temp = 1
    return temp

def element_compare(fst_el, scnd_el):
    if(fst_el == "Вогонь"):
        return compare_bolean(FIRE, scnd_el)
    elif(fst_el == "Вода"):
        return compare_bolean(WATER, scnd_el)
    elif(fst_el == "Камінь"):
        return compare_bolean(STONE, scnd_el)
    elif(fst_el == "Папір"):
        return compare_bolean(PAPER, scnd_el)
    elif(fst_el == "Колодязь"):
        return compare_bolean(KOLODJAZ, scnd_el)
    elif(fst_el == "Ножиці"):
        return compare_bolean(SCISSORS, scnd_el)

def main_battle(element):
    my_damage = 0
    opponent_damage = 0
    opponent_choosen = THINGS[random.randint(0, 5)]
    boolean = element_compare(element, opponent_choosen)
    if(boolean == 1):
        opponent_damage = damage_processor(opponent_choosen)
    elif(boolean == 0):
        boolean = element_compare(opponent_choosen, element)
        if(boolean == 1):
            my_damage = damage_processor(element)
        elif(boolean == 0):
            print("Ніхто не наніс урону, нічия.")
    
    print("Ви вибрали " + element + " і нанесли противнику " + str(my_damage) + " одиниць урону")
    print("Противник вибрав " + opponent_choosen + " і наніс вам " + str(opponent_damage) + " одиниць урону")
    global MY_HP
    global OPPONENT_HP
    MY_HP = MY_HP - opponent_damage
    OPPONENT_HP = OPPONENT_HP - my_damage
    if(MY_HP <= 0):
        print("Ви програли:(")  
        prt()
    if(OPPONENT_HP <= 0): 
        print("Ви виграли:)")
        prt()
    print("У вас залишилося " + str(MY_HP) + " ХП")
    print("У противника залишилося " + str(OPPONENT_HP) + " ХП")
    

    random_processor()

def start(first, second, third):
    print("Виберіть номер елемента: \n" + "1)" + first + "\n2)" + second + "\n3)" + third)
    choosen = int(input())
    if(choosen == 1):
        choosen = first
        main_battle(choosen)
    elif(choosen == 2):
        choosen = second
        main_battle(choosen)
    elif(choosen == 3):
        choosen = third
        main_battle(choosen)
    else:
        print("Введіть правильне число")
        start(first, second, third)

def prt():
    global MY_HP
    global OPPONENT_HP
    MY_HP = 100
    OPPONENT_HP = 100
    print("Привіт!")
    print("Виберіть цифру з меню:\n1) Почати\n2) Вийти")
    choice = int(input())
    if(choice == 1):
        random_processor()
    elif(choice == 2):
        print("Дякуємо за гру:)")
    else:
        print("Виберіть 1 або 2")


prt()