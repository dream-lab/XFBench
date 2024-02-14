from python.src.utils.classes.commons.serwo_objects import SerWOObject
import logging

def user_function(xfaas_object) -> SerWOObject:
    try:
        body = xfaas_object.get_body()
        if 'size_list' not in body:
            retval = {"result": "OK! Done!"}
            return SerWOObject(body=retval)
        size_list = body['size_list']
        base = body['base']
        input = body['input']
        target_size = size_list[0]
        input = base * target_size
        
        if len(size_list)>1:
            upd_list = size_list[1:]
            retval = {"size_list": upd_list, "base": base, "input": input}
        else:
            retval = {"result": "OK! Done!","input": input}
        
        return SerWOObject(body=retval)       

    except Exception as e:
        logging.info('in comm_stress: ',e)
        return None