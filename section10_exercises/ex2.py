try:
    f_animals = open('animals.txt')

    a_animals = f_animals.readlines()
    a_animals.sort()

    f_animals.close()
except:
    print("Could not open file animals.txt for reading.")

try:
    s_animals = open('animals-­sorted.txt', 'w')

    for animal in a_animals:
        animal = animal.rstrip()
        animal = animal + "\n"
        s_animals.write(animal)

    s_animals.close()
except:
    print("Could not open file animals-sorted.txt for writting.")



