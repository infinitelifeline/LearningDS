import numpy as np
def Guessing_Number(number: int = np.random.randint(1, 101)) -> int:
    '''Устанавливаем случайное число, 

    Args:
        number (int, optional): hidden number. Defaults to np.random.randint(1, 101).

    Returns:
        int: Количество попыток
    '''
     
    count = 0
    max_number = 1000
    min_number = 0
    predict_number = np.random.randint(1, 101)
    
    while True:
        
        count += 1
        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
            
        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        
        else:
            break #Выход в случае определения числа
        
    return count
    
def score_game(Guessing_Number) -> int:
    count_ls = [] #Список для кол-ва подсчетов
    
    np.random.seed(1) #Сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(10000))
    
    for number in random_array:
        count_ls.append(Guessing_Number(number))
        
    score = int(np.mean(count_ls)) #Подсчет среднего количества попыток
    print(f'You tried {score} times')

score_game(Guessing_Number)
