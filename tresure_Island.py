
death = ('''                 ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `# 
   
   ''')

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                  ''')


print("Welcome to the treasure island. \n")
print("Your mission is to find the treasure. \n")
door = input("You are insede a castle, what the door do you want to open 'right' or 'left' ? \n").lower()
if(door == "left"):
    room = input("You get inside a giant room, in the middle of that has a river, do you 'swim' or 'wait' ?  \n").lower()
    if(room == "wait"):
        chest = input("After watting some time, you bump in a stone. \n That makes 3 Treasure's chests apper front-side of you \n wich you choose 'red' , 'blue' or 'yellow' ?  \n").lower()
        if(chest == "yellow"):
            print("You find the treasure. Congratilations you win.")
        elif(chest == "red"):
            print("When you open it a explosion happens")
            print(death)
        else:
            print("A lot of beasts get out of the chest and attacked you.")
            print(death)
    else:
        print("You are attacked by a crocodile and died")
        print(death)


else:
    print("You fall into a hole, so game over for you!!!")
    print(death)



