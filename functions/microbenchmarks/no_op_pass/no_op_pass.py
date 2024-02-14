from python.src.utils.classes.commons.serwo_objects import SerWOObject


def user_function(xfaas_object):
    data = xfaas_object.get_body()['data']
    body =  {"data":data}

    return SerWOObject(body=body)