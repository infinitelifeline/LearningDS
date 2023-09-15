"""guess the number"""
import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input('guess the number form 1 to 100: '))
    
    if predict_number > number:
        print('number must be lesser!')
    elif predict_number < number:
        print('number must be bigger!')
        
    else:
        print(f'You guessed it! it`s {number} in {count} tries')
        break