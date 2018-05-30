# Dictonaries
facts = {
    'Jeff': 'Is afraid of clowns.',
    'David': 'Is afraid of clowns.',
    'Jason': 'Can fly an airplane.'
}

for person, fact in facts.items(): 
    print('{} {}'.format(person, fact))

#for person in facts:
    #print('{} {}'.format(person, facts[person]))
    #print(person, facts[person])

print()

facts['Jason'] = 'Has crashed a glider.'
facts['Mellisa'] = 'Can play the mouth harp.'

for person, fact in facts.items(): 
    print('{} {}'.format(person, fact))