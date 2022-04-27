import numpy as np
import numpy as np
import random
from time import gmtime, strftime
import string
import time

def plc_data():
    data = {}
    data['timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    data['values'] = np.array({
        'v':random.randint(1,500),
        't':strftime("%Y-%m-%d %H:%M:%S", gmtime()),
        'q':random.choice([True,False]),
        'id': "".join( [random.choice(string.ascii_letters) for i in range(15)] )
    })
    return data

#print(type(plc_data),type(plc_data['values']))

def plc_data_2():
    data = {}
    data['timestamp'] = random.randint(1650607000000, 1650608000000)
    data['values'] = list({
        'v':random.randint(1,500),
        't':random.randint(1650607000000, 1650608000000),
        'q':random.choice([True,False]),
        'id': "".join( [random.choice(string.ascii_letters) for i in range(15)] )
    })
    return data