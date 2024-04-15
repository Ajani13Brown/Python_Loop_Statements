# Task 1: Loop Condition Exploration
#-- 'the prompt asked to "Write a while loop with a condition that will never be true (an infinite loop)."
#-- if a whlie lok has a false starting condition or a conditon that will never be true then the code just doesnt run?
#-- I assumed you mean a condition that will never be false (an infinite loop) if not i apologize for the confusion.

while True:
    cat_count = input('How many cats does old lady Phyllis have in her house?')

    if cat_count == '999':
        print('BINGO!! Great guess, your right!')
        break
    else:
        print('Sorry, Wrong answer guess again.')

# Task 2: Conditional Exit

hot_dogs = 0

while hot_dogs < 5:
    hot_dogs += 1
    print("Im having a hot dog, Ive only had", hot_dogs)
    
