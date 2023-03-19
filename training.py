'''from collections import OrderedDict
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages  = OrderedDict(sorted(data, key=lambda x: x[1]))
ordered_client_ages['Nikita'] = 25
del ordered_client_ages['Mark']
print(ordered_client_ages )'''

'''from collections import deque
from collections import defaultdict'''

'''clients = deque()
clients.append('Ivanov')
clients.append('Smirnov')
clients.append('Petrov')
clients.append('Semenov')

first_client = clients.popleft()
second_client = clients.pop()
print(first_client)
print(second_client)
print(clients)
del clients[1]
print(clients)'''

'''shop = deque([1, 2, 3, 4, 5])
print(shop)
shop.extendleft([11, 12, 13, 15])
print(shop)'''

'''limited = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
print(limited.count(4))'''

'''days = deque(maxlen=7)

for temp in temps:
    days.append(temp)
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
print("")
'''
'''temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]
def check(temps):
    temp = OrderedDict(sorted(temps, key= lambda x: -x[1]))
    return temp
print(check(temps))'''

'''users = [6, 18, 4, 7, 8, 8, 5, 18, 12, 17, 13, 15, 6, 7, 9, 17, 18, 8, 4, 11, 10, 8, 2, 10, 6, 10, 10, 9]
user = deque(users)
first = user.popleft()
user'''

'''def brackets(line):
    lst = deque()
    for sign in line:
        if sign == '(':
            lst.append(sign)
        elif sign == ')':
            if len(lst) == 0:
                return False    
            lst.pop()
    if len(lst) == 0:
        return True
    else:
        return False'''
    
'''cafes = OrderedDict(sorted(ratings, key=lambda x: (-x[1], x[0])))
'''

'''def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers
        '''
        
import numpy as np
'''arr = np.array([[14, 24, 521, 12],
                [14, 21, 41, 13],
                [31, 12, 42, 12]])
print(arr.ndim)'''

'''mystery = np.array([[-13586,  15203,  28445, -27117,  -1781, -17182, -18049],
       [ 25936, -30968,  -1297,  -4593,   6451,  15790,   7181],
       [ 13348,  28049,  28655,  -6012,  21762,  25397,   8225],
       [ 13240,   7994,  32592,  20149,  13754,  11795,   -564],
       [-21725,  -8681,  30305,  22260, -17918,  12578,  29943],
       [-16841, -25392, -17278,  11740,   5916,    -47, -32037]],
      dtype=np.int16)

elem_5_3 = mystery[5, 4]
last =mystery[5, 6]
line_4 =mystery[4]
col_2 = mystery[:, 5]
part = mystery[2:5, 3:6]
rev = mystery[::-1, -1]
trans = mystery.transpose()'''

mystery = np.array([ 12279., -26024.,  28745.,  np.nan,  31244.,  -2365.,  -6974.,
        -9212., np.nan, -17722.,  16132.,  25933.,  np.nan, -16431.,
        29810.], dtype=np.float32)

'''nans_index = np.isnan(mystery)
n_nan = sum(nans_index)
mystery_new = mystery
mystery_new[nans_index] = 0
mystery_int = np.int32(mystery)
array = np.sort(mystery)
table = array.reshape((5, 3), order='F')
col = table[:5, 1]'''


nans_index = np.isnan(mystery)
n_nan = sum(nans_index)
mystery_new = mystery
mystery_new[nans_index] = 0
mystery_int = np.int32(mystery)
array = np.sort(mystery)
table = array.reshape((5,3), order='F')
col = table[:, 1]
print(mystery_new)
