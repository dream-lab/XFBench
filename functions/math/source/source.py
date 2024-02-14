import random

# XFaaS specific imports
from python.src.utils.classes.commons.serwo_objects import SerWOObject

def user_function(xfaas_object):
    try:
        print("\n\n\n\n",xfaas_object)
        body = xfaas_object.get_body()
        if 'seed' in body and 'iters' in body:
            ub = body['upper_bound']
            returnbody = body
        else:
            seed = random.randrange(10000)
            iters = random.randrange(10000)
            iters = 1000
            ub = body['upper_bound']
            returnbody = {
                'seed': seed,
                'iters': iters,
                'upper_bound': ub
            }
        return SerWOObject(body=returnbody)
    except Exception as e:
        print(e)
        raise Exception("[SerWOLite-Error]::Error at user function")