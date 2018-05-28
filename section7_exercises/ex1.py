def get_todo(to_do_list):
    done = False
    while not done:
        u_input = input('Enter a task for your to­do list. Press <enter> when done: ')
        if len(u_input) == 0:
            done = True
        else: 
            to_do_list.append(u_input)
            print('To Do Added...')
    return to_do_list

def print_todos(to_do_list):
    print('')
    print('You need to do these things:')
    print('----------------------------')
    for things_to_do in to_do_list:
        print('{}'.format(things_to_do))

to_do_list = []
to_do_list = get_todo(to_do_list)
print_todos(to_do_list)