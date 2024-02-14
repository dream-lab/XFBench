import argparse
import os
import json
parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)
parser.add_argument("--parallel_branches",dest='parallel_branches',type=int,help="Number of parallel branches")
args = parser.parse_args()



if __name__ == "__main__":
    # Create parallel branches
    parallel_branches = args.parallel_branches
    print(parallel_branches)
    out_path = os.getenv("XFAAS_WF_DIR") +f"/workflows/microbenchmarks/parallelism_stress_{parallel_branches}/workflow.json"
    out_dict = {}
    out_dict["WorkflowName"] = f"parallelStress{parallel_branches}"
    out_dict["Nodes"] = []
    out_dict["Edges"] = []
    nodes = ["Source","Sink"]

    new_nodes = []
    for i in range(parallel_branches):
        nodes.append(f"Branch{i}")
        new_nodes.append(f"Branch{i}")
    src_edges ={
        "Source": new_nodes
    }
    out_dict["Edges"].append(src_edges)
    for i in range(parallel_branches):
        branch_edges = {
            f"Branch{i}": ["Sink"]
        }
        out_dict["Edges"].append(branch_edges)

    

    node_obj = {
        "microbenchmarks": "no_op_pass",
        "code":"NOOP",
        "nodes":nodes
    }
    out_dict["Nodes"].append(node_obj)
    edges = []
    

    print(out_dict)


    with open(out_path, "w") as f:
        json.dump(out_dict, f, indent=4)