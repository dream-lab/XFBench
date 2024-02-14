import os
from random import randint
from python.src.utils.classes.commons.serwo_objects import SerWOObject


def stress_fs(count):
    xd = randint(1000, 9999)
    fname = f'/tmp/testfile{xd}.txt'
    print(fname)
    for _ in range(count):
        write_file(fname)
        read_file(fname)
    os.remove(fname)

def write_file(fname):
    MEGA = 2 ** 20
    f = open(fname, "w")
    a = ' ' * (1 * MEGA)  # Change the 512 to a value you want to write
    for _ in range(50):
        f.write(a)
    f.close()

def read_file(fname):
    f = open(fname, "r")
    l = f.read()

def user_function(serwoObject) -> SerWOObject:
    try:
        stress_fs(1)
        ret_val = {"data": "test"}
        print('io complete')

        s = SerWOObject(body=ret_val)
        return s
    except Exception as e:
        print('in iostress: ',e)
        return None
