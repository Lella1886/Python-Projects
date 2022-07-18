print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to Treasure Island!\n Your goal is to find the treasure.')

choice1 = input('You come to a crossroads in a dark forest. Do you go left or right?')
left_or_right = choice1.lower()
if left_or_right == 'left':
    choice2 = input('The path takes you to a river it looks deep enough to swim but you notice\nstrange shadows in the water. \nDo you swim or wait for a boat (swim or wait)?')
    swim_or_wait = choice2.lower()
    if swim_or_wait == 'wait':
        print('Shoto Todoroki arrives (lucky you) and creates an ice bridge to help you cross. Before he leaves he gives you his number(I would do ANYTHING to be you right now')
        choice3 = input("You arrive on a small island (and memorise Shoto's number) then you enter a small warehouse. There are 3 doors one with a symbol displaying a pair of blue and white wings, the second door has  a symbol with two red roses\nand the third dislays a symbol with a green horse head.\nDo you choose door number 1, 2 or 3?")
        if choice3 == '1':
            print("Megumi Fushiguro is waiting behind the door with one of Sukuna's fingers! You escape together and meet up with Shoto for a date!!!!")
        elif choice3 == '2':
            print("Adam is waiting behind the door and hits you with his skateboard just like he did with Cherry. Langa comes and saves you but you leave without the intel you came here for. You go on a date with Langa (you're still insanely lucky to get Langa <3")
        else:
            print("Bakugo is waiting behind the door and kills you using his quirk for beating him in the Sports Festival.\nGame Over!")
    else:
        print('The shadows were Special Grade Cursed Spirits! No Jujutsu Scorcerers show up and they kill you.\n Game Over!')
else: print('You stumbled into the League of Villians hideout where they were experimenting with Titans.\nBefore you could escape Dabi kills you with his flames. Game Over!')

    