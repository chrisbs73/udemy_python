def get_user_input(req):
    """
    Get input from user, return value
    """
    answer = input('Enter a {} to be used... '.format(req))
    return answer

def the_story():
    """
    Print out the story based on the user input
    """
    noun = get_user_input('noun')
    verb = get_user_input('verb')
    adj = get_user_input('adjective')

    print('')
    print('See {} {}.'.format(noun, verb))
    print('{} {} {}.'.format(verb.capitalize(), noun, verb))
    print('{} {} {}.'.format(verb.capitalize(), adj, noun))

the_story()