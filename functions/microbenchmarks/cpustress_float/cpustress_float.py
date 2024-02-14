import multiprocessing
import time
import sys
import random
from python.src.utils.classes.commons.serwo_objects import SerWOObject

def stresser():
    
    f = random.random()
    for i in range(100):
        g = random.random()
        h = random.random()

        f = f*g + h
        
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
