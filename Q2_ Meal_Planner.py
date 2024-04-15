week= ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

time= ['breakfast','lunch','dinner']

brkfst= ['breakfast sandwich', 'pancakes','muffin']

lun =['turkey sandwich', 'fruit salad', 'tacos']

din = ['chicken parm', 'rice and veggie', 'pepperoni pizza']

import random

for day in week:
    for meal in time:
        if meal == 'breakfast':
            print(day, 'for', meal, 'I ate', random.choice(brkfst))
        elif meal == 'lunch':
            print(day, 'for', meal, 'I ate', random.choice(lun))
        elif meal == 'dinner':
            print(day, 'for', meal, 'I ate', random.choice(din))