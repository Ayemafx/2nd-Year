player_name = input('Enter the name of the player')
total_runs = int(input('Enter total runs made by the player'))
total_match_played = int(input('Enter total number of matches played'))


def finding_average():
    average = int(total_runs / total_match_played)
    if (average <= 100) and (average >= 80):
        print(f'Your average runs is {average}')
        print('You are a Grade A player')
        print('Your salary is above 1 lac')

    elif (average < 80) and (average >= 50):
        print(f'Your average runs is {average}')
        print('You are a Grade B player')
        print('Your salary below 1 lac & above 50K')

    elif (average < 50) and (average > 0):
        print(f'Your average runs is {average}')
        print('You are a Grade C player')
        print('Your salary is below 50K')

    else:
        print('Your average is invalid')


finding_average()



