# From: https://github.com/obi-wan-shinobi/Stress-test

from python.src.utils.classes.commons.serwo_objects import SerWOObject
import random
def alloc_max_str(memory):
    """
    Function to load memory by assigning string of requested size
    Arguments:
        memory: amount of memory to be utilized in MB
    Returns: 
        a : String of size 'memory'
    """
    # Adjust increments to a smaller value if needed, maybe 1 MB.
    MEGA = 2 ** 20
    i = 1
    a = ''
    while i<25:
        try:
            a = ' ' * (i * 4 * MEGA)
            rnd_index = random.randint(0, len(a) - 1)

            b = a[rnd_index]
            del a
        except MemoryError as e:
            # logging.info(f'mem excep = {e}')
            break
        i += 1
    # return a


def user_function(serwoObject) -> SerWOObject:
    try:
        # body = serwoObject.get_body()
        print("stress memory 128MB, sending 25KB")
        alloc_max_str(128)
        ret_val = {"data": "test"}
        print('memstress complete')
        s = SerWOObject(body=ret_val)

        return s
    except Exception as e:
        print('in memstress ',e)
        return None
