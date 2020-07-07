import time  # import time to sleep some times
import random  # import random to select random objects
# Confugre List Of Objects
Places = ['Forest', 'Desert', 'sea', 'park']
Weapons = ['Sword', 'Knife', 'Gun', 'Rock']
Forest_Monsters = ['Bear', 'Poisonous frog', 'Lion', 'Wolf', 'Giant spider']
Desert_Monsters = ['Ostrich', 'Killer bees', 'Snake', 'Wild dog']
sea = ['Squid', 'Shark', 'Octopus', 'Sea snake']
park = ['Rabbit', 'Butterfly', 'Squirrel', 'Giraffe']
Game_Result = ['Won', 'Lost']
UserResponse = ['yes', 'no', 'y', 'n']
Monster = ''
# End Configuration
# Define Function To print Messages


def GetUserchoice(Input):
    if choice.lower() == ' Forest'.lower() or\
        choice.lower() == 'F'.lower() or\
            choice == '1':
            return 'Forest'
    elif choice.lower() == 'Desert'.lower() or \
        choice.lower() == 'D'.lower() or \
            choice == '2':
            return 'Desert'
    elif choice.lower() == 'sea'.lower() or \
        choice.lower() == 'S'.lower() or \
            choice == '3':
            return 'sea'
    elif choice.lower() == 'park'.lower() or \
        choice.lower() == 'P'.lower() or \
            choice == '4':
            return 'park'
    else:
        return ''


def GetUserMonster(Userchoice):
    if Userchoice == 'Forest':
        Monster = random.choice(Forest_Monsters)
        print(Monster)
    if Userchoice == 'Desert':
        Monster = random.choice(Desert_Monsters)
        print(Monster)
    if Userchoice == 'sea':
        Monster = random.choice(sea)
        print(Monster)
    if Userchoice == 'park':
        Monster = random.choice(park)
        print(Monster)


def PrintSleep(msg, seconds):
    print(msg + '\n')
    time.sleep(seconds)


def ChangeWeapon():
    changerequest = input('would you like to change weapon?\n')
    while changerequest not in UserResponse:
        print('Invalid input please choose yes or no or y or n')
        changerequest = input('would you like to change weapon\n')
    if changerequest == 'yes' or changerequest == 'y':
        weaponchoosed = random.choice(Weapons)
        print(weaponchoosed)
# Game Will Start
RetryGame = 'y'
while RetryGame == 'y' or RetryGame == 'yes':
    PrintSleep('\nWelcome to the game of adventures ', 2)
    PrintSleep('takes you to another world of fun and thrill', 2)
    PrintSleep('you have to choose wisley so you can win', 2)
    name = input('Please Enter Your Name To Start Game \n')
    while name.strip() == '':
        name = input('Please Enter Your Name To Start Game \n')
    time.sleep(1)
    print('\nPlease Choose one of the haitats below \n')
    time.sleep(1)
    for place in Places:
        print(place)
        time.sleep(1)
    choice = ''
    while choice not in Places:
        msg = '\nfor forest write f or forest or 1 \
        \nfor desert write desert or d or 2 \
        \nfor sea write sea or o or 3 \
        \nfor park write park or p or 4\n'
        choice = input(msg)
        choice = GetUserchoice(choice)
    time.sleep(2)
    print('you have a weaponized: ')
    weaponchoosed = random.choice(Weapons)
    print(weaponchoosed)
    ChangeWeapon()
    print(
        '\nyou are now in the:' + choice + ' and you have a: ' + weaponchoosed
    )
    time.sleep(4)
    print('now you see a: ')
    GetUserMonster(choice)

    time.sleep(2)
    PrintSleep('you used the weapon to eliminate the animal', 2)
    if (weaponchoosed == 'Rock' or weaponchoosed == 'Sword' or
        weaponchoosed == 'Gun' or weaponchoosed == 'Knife')\
            and Monster == 'Rabbit':
        print('you Won')
        time.sleep(2)
        print ('Game Over')
    elif choice == 'park':
        print('you won')
        time.sleep(2)
        print ('Game Over')
    else:
        print('you ' + random.choice(Game_Result))
        time.sleep(2)
        print ('Game Over')
    RetryGame = input(
        '\nWould You Like to try again for yes write y for no write n'
        )
    while RetryGame not in UserResponse:
        print('Invalid input please choose yes or no or y or n')
        RetryGame = input(
            'Would You Like to try again for yes write y for no write n\n'
            )
