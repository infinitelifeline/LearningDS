import numpy as np
def Guessing_Number(number: int = 1) -> int:
     
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count
    
#def score_game(number: int=3) -> int:
    tries = []
    count_ls = []
    #np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(5))
    for number in random_array:
        count_ls.append(Guessing_Number(number))
        
    score = int(np.mean(count_ls))
    print(f'You tried {score} times')

Guessing_Number(5)
