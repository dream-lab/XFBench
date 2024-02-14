import json
import sys
import subprocess
import os
import shutil
import argparse
import random

parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)
parser.add_argument("--function-class",dest='function_class',type=str,help="Function class")
parser.add_argument("--function-name",dest='function_name',type=str,help="Function name")
parser.add_argument("--function-code",dest='function_code',type=str,help="Function code")
parser.add_argument("--node_name",dest='node_name',type=str,help="Node name")
args = parser.parse_args()

def get_func_path(func_name, category_name):
    root_dir = os.getenv("XFAAS_WF_DIR")
    folder_path = f'{root_dir}/functions/{category_name}/' + func_name
    return folder_path

def get_func_file_name(func_name):
    return f'{func_name}.py'

def get_wf_dir(dag_path):
    return os.path.dirname(dag_path)

def copy_folder(src, dst):
    try:
        if not os.path.exists(dst):
            shutil.copytree(src,dst)
        else:
            ##remove the folder and copy again
            shutil.rmtree(dst)
            shutil.copytree(src,dst)
    except Exception as e:
        print(f"Error copying '{src}': {e}")

def create_dag_file(function_class,function_name,function_code,node_name,wf_base_path):
    # Load node data
    nodes = [{
            function_class:function_name,
            "nodes":[node_name],
            "code":function_code
        }]
    idx = 0
    res = []
    for item in nodes:
        cat_name = list(item.keys())[0]
        func_name = list(item.values())[0]
        code = item['code']
        func_nodes = item['nodes']
        print(list(item.values()))

        # Get relevant paths
        func_path = get_func_path(func_name, cat_name)
        func_file = get_func_file_name(func_name)
        
        dst_path = os.path.join(f'{wf_base_path}/workflow-gen/{func_name}')

        # Create node for each func
        idx = idx + 1
        # Create src_gen folder
        copy_folder(func_path, dst_path)
        ## delete readme if exists  
        readme_path = f"{dst_path}/README.md"
        if os.path.exists(readme_path):
            os.remove(readme_path)

        memory = f"{dst_path}/memory.txt"
        if os.path.exists(memory):
            os.remove(memory)
        
        ##delete samples if exists
        samples_path = f"{dst_path}/samples"
        dst_path_2 = f'{wf_base_path}/workflow-gen'
        ## copy samples to dst_path
        copy_folder(samples_path, f"{dst_path_2}/samples")
        if os.path.exists(samples_path):
            shutil.rmtree(samples_path)

        memory = 128
        if func_name == 'resnet':
            memory = 512
        if func_name == 'alexnet' or func_name == 'memstress':
            memory = 256
        if len(func_nodes) == 1:
            node = {
                        "NodeId": f"{idx}",
                        "NodeName": f"{func_nodes[0]}",
                        "Path": f"{dst_path}",
                        "EntryPoint": f"{func_file}",
                        "CSP": "NA",
                        "MemoryInMB": memory,
                        "Code": f"{code}"
                    }
            res.append(node)
        

    # dump to new dag.json file
    data = {}
    data["Nodes"] = res
    data["Edges"] = []
    ##remove all underscores and do camel case
    function_class = function_class.replace("_","")
    function_name = function_name.replace("_","")
    data['WorkflowName'] = f"{function_class}{function_name}"
    
    dag_path = f"{wf_base_path}/workflow-gen/dag.json"

    with open(dag_path, 'w') as file:
        ret = json.dumps(data,indent=4)
        file.write(ret)
    
    # Copy samples of first node to wf_dir
    # copy_folder(f"{res[0]['Path']}/samples/", f"{wf_dir}/samples/")

# Specify the path to your JSON file

def build(function_class,function_name,function_code,node_name,wf_base_path):
    
    create_dag_file(function_class,function_name,function_code,node_name,wf_base_path)


function_class = args.function_class
function_name = args.function_name
function_code = args.function_code
node_name = args.node_name

wf_base_path = f"{os.getenv('XFAAS_WF_DIR')}/workflows/singleton_workflows/{function_class}/{function_name}"
##mkdirs if not exists
if not os.path.exists(wf_base_path):
    os.makedirs(wf_base_path)

build(function_class,function_name,function_code,node_name,wf_base_path)
