'''
print("tohle se vypsalo")
celeCislo = 5
print(celeCislo)
print(type(celeCislo))
celeCislo = 5.5
print(celeCislo)
print(type(celeCislo))
# promenna1 = "tohle je string"
# tohle je jednoradkovy komentar
\'''
tohle je viceradkovy komentar
\'''
promenna1 = 'tohle je string'
print(promenna1)
print(type(promenna1))
promenna2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(promenna2[0])
print(promenna2[5])
promenna2.append(5)
print(promenna2)
var = False
var = True
print(None)
slovnik = {
    1: "aho'j",
    "druhy": 2,
    2.5: None,
}
print(slovnik)
print(promenna2)
print(type(promenna2))
promenna3 = (1, 2, 3, 4, 5)
print(promenna3)
print(type(promenna3))
slovnik = {
    'prvni': "aho'j",
    "druhy": 2
}
print(slovnik['druhy'])
slovnik['treti'] = 'nazdar lidi'
print(slovnik['treti'])
print(slovnik)
print(type(slovnik))
var1 = ''
var2 = 'ahoj'
print(var1 == False)
var = (5 + 5) is 11
if var:
    print("je to pravda")

var = 'tvoje máma'
if var is 5:
    print('je to 5')
    print('tohle je furt 5')
# tohle je prostě else if
elif var is 6:
    print('je to 6')
    print('tohle je furt 6')
elif var is 7:
    print('je to 6')
    print('tohle je furt 6')
elif var is 'tvoje máma':
    print('je to tvoje máma')
elif var is 8:
    print('je to 6')
    print('tohle je furt 6')
else:
    print('neni to 5, ani 6')
'''
'''
def addNumbers(x, y):
    print("zavolala se funkce, x=" + str(x))
    return x + y
def addNumber(x, y=1):
    print("zavolala se funkce, x=" + str(x))
    return x + y

var = 7
#print(addNumber(5, var))
#print(addNumber(y=5, x=var))
#print(addNumber(4))
# x = input('zadej cislo\n')
# print(x)
arr = [2, 4, 6, 8, 10]
dic = {
    '5': 1, 
    '7': 'nazdar'
\}
for key, value in dic.items():
    print(key, value)
'''

'''
import sys
position = [5, 5]
actions = {
    'vlevo': (-1, 0),
    'vpravo': (1, 0),
    'nahoru': (0, 1),
    'dolu': (0, -1),
}
while True:
    print('povolene akce jsou: ' + str(list(actions.keys())))
#    action = input('kam chces jit\n')
#    action = sys.stdin.read(1)

    if not action in actions.keys():
        print('neznamy vstup')
        continue

    movement = actions[action]
#    position[0] = position[0] + movement[0]
#    position[1] = position[1] + movement[1]
# vyse uveden jsem zrefactoroval na cyklus
    for i, value in enumerate(position):
        position[i] = position[i] + movement[i]
    print('tvoje pozice je: ' + str(position))
'''
'''
def my_function(access_global=False):
    global a
    a = 10
    print(a)
a = 5
print(a)
my_function()
print(a)
my_function(True)
print(a)
'''
'''
def my_function():
    return 5, 10, 15
a, b, c = my_function()
result = my_function()
a, b, c = result
print(b, c, a)
print(result)
print(type(result))
'''


class Inventory:
    capacity = 0
    items = []

    def __init__(self, capacity=2):
        self.capacity = capacity

    def add_item(self, item):
        if len(self.items) >= self.capacity:
            # print('Backpack is full.')
            # return
            raise ValueError('Backpack is full')
        self.items.append(item)

    def remove_item(self, item):
        if not item in self.items:
            print('I do not have ' + item)
            return
        self.items.remove(item)

    def introduce_myself(self):
        return "I am inventory with capacity " + str(self.capacity)

    def __len__(self):
        print("hele, zavolal se __len__. Magic.")
        return len(self.items)


class InfiniteInventory(Inventory):
    def add_item(self, item):
        self.items.append(item)

    def introduce_myself(self):
        return "I am infinite inventory"


class Character:
    inventory = None
    name = None
    race = None

    def __init__(self, name, race):
        print("hele, zavolal se __init__. Magic.")
        self.inventory = Inventory(10)
        self.name = name
        self.race = race

    def introduce_myself(self):
        if self.race is 'murloc':
            return 'Rwlrwlrwl'

        return "I am " + self.name + " and this my inventory: " + self.inventory.introduce_myself()

    def show_inventory(self):
        return "my inventory contains " + str(len(self.inventory.items)) + " items: " + str(self.inventory.items)

    # tohle se zavola, kdykoli to pretypuju na string
    def __str__(self):
        print("hele, zavolalo se __str__. Magic.")
        return self.introduce_myself()


# creating some characters
character1 = Character(name='Thrall', race='orc')
character2 = Character(name='Jaina', race='human')
character3 = Character(name='Korialstraz', race='dragon')
character4 = Character(name='Cookie', race='murloc')

'''
# introducing ourselves
print(character2.name)
character2.name = 'Medivh'
print(character2.name)
print(character2.introduce_myself())
print(character4.introduce_myself())
'''

# playing with inventory
character2.inventory.capacity = 3
print(character2.inventory.introduce_myself())
# character2.inventory = InfiniteInventory()
print(character2.inventory.introduce_myself())
print(character2.show_inventory())
character2.inventory.add_item('healing potion +5')
print(character2.show_inventory())
character2.inventory.add_item('mana potion +5')
character2.inventory.add_item('sword')
# character2.inventory.remove_item('shield')
try:
    character2.inventory.add_item('hearthstone')
except ValueError:
    print("Máme plno, sorryjako.")
print(character2.show_inventory())

'''
# malé hrátky s dělením nulou
try:
    5 / 0
except ZeroDivisionError:
    print("pokusil ses dělit nulou")
'''

'''
# playing with magic methods
print(character1)
print(len(character1.inventory))
'''