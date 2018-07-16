def catsays (cattext):
    print ('          {}'.format("_"*len(cattext)))
    print ('        < {} >'.format(cattext))
    print ('          {}'.format("-"*len(cattext)))
    print ('        /')
    print (' /\_/\ /')
    print ('( o.o )')
    print (' > ^ <')

def main():
    user_input = input('Cat says? ')
    len_user_input = len(user_input)
    catsays(user_input)

if __name__ == '__main__':
    main()