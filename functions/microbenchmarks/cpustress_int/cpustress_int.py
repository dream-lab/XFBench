import multiprocessing
import time
import sys
from python.src.utils.classes.commons.serwo_objects import SerWOObject
import random
def stresser():
    f = random.randint(0, 100000)
    for i in range(100):
        g = random.randint(0, 100000)
        h = random.randint(0, 100000)

        f = f * g + h
        
    return

def user_function(serwoObject) -> SerWOObject:
    try:
        cores_stress = 1
        time_stress = 10
        
        for i in range(time_stress):
            stresser()
        ret_val = {"data": "test"}
        return SerWOObject(body=ret_val)
    except Exception as e:
        print('in cpustress: ',e)
        return None
