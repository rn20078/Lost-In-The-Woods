import random
import time

while True:
    score = 0

    # Function to add 5 to the existing score if the user makes a good choice
    def add_score():
        global score
        score += 5
        print_pause('Your score is: ' + str(score))
        return score

    # Function to subtract 5 from the existing score if the user makes a bad choice
    def subtract_score():
        global score
        score -= 5
        print_pause('Your score is: ' + str(score))
        return score

    # Function to print a message and pause 2 sec afterwards
    def print_pause(message, duration=2):
        print(message)
        time.sleep(duration)

    # Function to check whether the user wants to play again
    def play_again():
        choice = input("Do you want to play again? (yes/no) ")
        if choice.lower() == "yes":
            print_pause("Let's start the game!")
            return True
        elif choice.lower() == "no":
            print("Too bad :(")
            return False
        else:
            print_pause("Invalid input. Please enter 'yes' or 'no'.")
            play_again()

    while True:
        def introduction():
            print_pause('You were driving your car alone through the woods far from civilization.')
            print_pause('Suddenly your car breaks down.')
            print_pause('With no cellular signal or help nearby, you try to find the nearest town to reach out for help.')
            print_pause('You get out of the car and walk straight until you reach a fork in the road.')
            print_pause('Your current score is 0')
            directions = ['1-Continue walking straight', '2-Turn right', '3-Turn left']
            print_pause(directions)

        introduction()

        result_1 = 'empty'

        # Function that randomizes results
        def result1():
            answer = input('please input 1, 2 or 3: ')
            while True:
                if answer in ['1', '2', '3']:
                    x = 'You walk deep into the never-ending woods, and you get lost. Game Over, better luck next time'
                    y = 'You find yourself in a clearing, and in front of you is a cave'
                    z = 'You walk for a while until you find another fork in the road'
                    possibilities = [x, y, z]
                    global result_1
                    result_1 = random.choice(possibilities)
                    if result_1 == x:
                        print_pause(result_1)
                        play_again()
                        break
                    else:
                        print_pause(result_1)
                        return result_1
                else:
                    print_pause('Invalid input')
                    answer = input('Enter a valid input: ')

        result1()

        result_2 = 'empty'

        def result2():
            if result_1 == 'You walk for a while until you find another fork in the road':
                directions = ['1-Turn right', '2-Turn left']
                print_pause(directions)
                answer = input('please input 1 or 2: ')
                while True:
                    if answer in ['1', '2']:
                        a = 'After walking for what felt like an eternity, you see your car again. '
                        b = 'You walk for a while when you see it is getting dark. '
                        possibilities = [a, b]
                        global result_2
                        result_2 = random.choice(possibilities)
                        if result_2 == a:
                            print_pause(a + 'You have returned to your starting point.')
                            subtract_score()
                            print_pause('It has already become pitch black, you lost')
                            play_again()
                            break
                        elif result_2 == b:
                            print_pause(b)
                            add_score()
                            result = 'You decide to use your flashlight but your phone battery is about to die'
                            print(result)
                            return result
                    else:
                        print_pause('Invalid input')
                        answer = input('Enter a valid input: ')

        result = result2()

        # User arrives at a town
        def arrival():
            print_pause('Your heart starts racing. But...there\'s a ray of hope')
            print_pause('You see car headlights passing by quickly in the distance.')
            print_pause('You\'ve found a small town. You dash to the nearest payphone and get help')
            print_pause(add_score())
            print_pause('Congratulations!! You\'ve successfully made it to the end!!')
            print_pause('You won!')

        def result3():
            if result == 'You decide to use your flashlight but your phone battery is about to die':
                choices = ['1-Turn your flashlight on anyway and take off running',
                           '2-Run straight without flashlight']
                print_pause(choices)
                answer = input('Please input 1 or 2: ')
                while True:
                    if answer in ['1', '2']:
                        c = 'Within 20 minutes, your battery dies.'
                        d = 'You run in straight path hoping you\'d arrive somewhere where you can reach out for help.'
                        if answer == '1':
                            print_pause(c)
                            arrival()
                            play_again()
                            break
                        elif answer == '2':
                            print_pause(d)
                            print_pause('But soon it becomes pitch black and you can\'t see the way anymore')
                            print_pause('It wasn\'t the best idea not to use your flashlight')
                            print_pause(subtract_score())
                            arrival()
                            play_again()
                            break
                        else:
                            print_pause('Invalid input')
                            answer = input('Enter a valid input: ')

        result3()

        def result4():
            while True:
                if result_1 == 'You find yourself in a clearing, and in front of you is a cave':
                    directions = ['1-Go inside the cave', '2-Go left and walk along the tree line']
                    print_pause(directions)
                    answer = input('please input 1 or 2: ')
                    if answer in ['1', '2']:
                        if answer == '1':
                            print_pause('You get lost in the cold, dark cave')
                            subtract_score()
                            print_pause('You lost. Better luck next time')
                            play_again()
                            break
                        elif answer == '2':
                            print_pause('You walk for a while then you notice it is getting dark')
                            result2 = 'You decide to use your flashlight but your phone battery is about to die'
                            print_pause(result2)
                            add_score()
                            choices = ['1-Turn your flashlight on anyway and take off running',
                                       '2-Run straight without flashlight']
                            print_pause(choices)
                            answer = input('Please input 1 or 2: ')
                            while True:
                                if answer in ['1', '2']:
                                    c = 'Within 20 minutes, your battery dies.'
                                    d = 'You run in straight path hoping you\'d arrive somewhere where you can reach out for help.'
                                    if answer == '1':
                                        print_pause(c)
                                        arrival()
                                        return play_again()
                                    elif answer == '2':
                                        print_pause(d)
                                        print_pause('But soon it becomes pitch black and you can\'t see the way anymore')
                                        print_pause('It wasn\'t the best idea not to use your flashlight')
                                        print_pause(subtract_score())
                                        arrival()
                                        play_again()
                                        break
                                    else:
                                        print_pause('Invalid input')
                                        answer = input('Enter a valid input: ')
                    else:
                        print_pause('Invalid input. Please enter 1 or 2.')

        result4()

        break