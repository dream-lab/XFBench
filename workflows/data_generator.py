import json
import os
import random
import string
## create a string with given data size in kilobytes
def create_data_string(data_size):
    data_size = data_size * 1024
    data_string = ""
    for i in range(data_size):
        ## generate a random character

        data_string += random.choice(string.ascii_letters)
        
    return data_string

data_sizes = [1,4,16,28,29,32,40,44,50,60,63,70,128,240,255,300,480,499,640,1024,4096,8192,9216,10240,16384]
for data_size in data_sizes:
    data_string = create_data_string(data_size)
    if data_size == 29 or data_size == 63 or data_size == 255 or data_size == 499:
        data_size += 1
    samples_path = f"/Users/varad.kulkarni/xfaas/xfaas-workloads/workflows/microbenchmarks/communication_stress/samples/{data_size}KB/input/"
    samples_out_path = f"/Users/varad.kulkarni/xfaas/xfaas-workloads/workflows/microbenchmarks/communication_stress/samples/{data_size}KB/output/"
    os.makedirs(samples_path, exist_ok=True)
    os.makedirs(samples_out_path, exist_ok=True)
    samples_path = samples_path + "input.json"
    samples_out_path = samples_out_path + "output.json"
    body = {
        "data": data_string
    }
    with open(samples_path, 'w') as file:
        ret = json.dumps(body,indent=4)
        file.write(ret)
    with open(samples_out_path, 'w') as file:
        ret = json.dumps(body,indent=4)
        file.write(ret)
    print(f"Created {data_size}KB data string")
    data_size = data_size * 4

