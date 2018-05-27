# get user input
travel_distance = int(input('How many miles would you like to travel? '))

if travel_distance >= 300: 
    print('I think you should fly - {} miles is a long way.'.format(travel_distance))
elif travel_distance >= 3: 
    print('I think you should drive - {} miles isn\'t that far.'.format(travel_distance))
else:
    print('I think you should walk - {} miles is really close.'.format(travel_distance))

