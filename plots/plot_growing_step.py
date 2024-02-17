import argparse
from collections import defaultdict
import os
import json
import statistics
import numpy as np


from matplotlib import pyplot as plt
parser = argparse.ArgumentParser(
    prog="ProgramName",
    description="What the program does",
    epilog="Text at the bottom of help",
)
parser.add_argument("--wf-user-directory", help="Path to the user directory")


def copy_pdf_file(src,dest):
    os.system(f"cp {src} {dest}")

def read_log_file(log_file_path):
    with open(log_file_path, "r") as file:
            loglines = [json.loads(line) for line in file.readlines()]
    return loglines

def init_dict(logs):
    distribution_dict = dict(
        client_overheads=[],
        functions=defaultdict(list),
        edges=defaultdict(list),
        wf_invocation_id = []
    )
    nodes = ["1"]
    for log in logs:
        wf_invocation_id = log["workflow_invocation_id"]
        distribution_dict["wf_invocation_id"].append(wf_invocation_id)
        distribution_dict["client_overheads"].append((int(log["invocation_start_time_ms"]) - int(log["client_request_time_ms"]))/1000)
        for u in [v for v in nodes]:
            exec_time = (log["functions"][u]["end_delta"])/1000 # seconds
            distribution_dict["functions"][u].append(exec_time)
        
    
    return distribution_dict

def plot_violin(god_list):
    

    fig, ax = plt.subplots()
    fig.set_dpi(400)
    ax.grid(True)
    ##box plot with means and medians ignore outliers
    ax.boxplot(god_list, showmeans=True, meanline=True, showfliers=False)
    # ax.boxplot(god_of_gods, showmeans=True, meanline=True, showfliers=False)
    # ax.violinplot(god_of_gods, showmeans=False, showmedians=True)
    xlabels = ["AWS Growing Step","Az Growing Step"]
    ax.set_xticks(np.arange(1,3))
    ax.set_xticklabels(xlabels)
    
    ax.set_ylabel('Execution Time (sec)')
    xfaas_dir = os.getenv('XFBENCH_DIR')
    plt.savefig(f"{xfaas_dir}/plots/growing_step_box.pdf",bbox_inches='tight')


if __name__ == "__main__":
    wf_user_directory = parser.parse_args().wf_user_directory + '/workflow-gen'

    xfaas_dir = os.getenv('XFBENCH_DIR')
    deployments_file_path = f"{xfaas_dir}/deployments.txt"

    deployments = []
    with open(deployments_file_path, 'r') as f:
        deployments = f.readlines()
        deployments = [x.strip() for x in deployments]
    i = 0
    os.makedirs(f"{xfaas_dir}/plots/growing_step_timelines", exist_ok=True)
    timeline_dir = f"{xfaas_dir}/plots/growing_step_timelines"
    god_list = []
    for deployment in deployments:
        log_file_dir = f"{wf_user_directory}/{deployment}/exp1/logs/"
        files = os.listdir(log_file_dir)
        log_file_path = f"{log_file_dir}/{files[0]}"
        plots_dir = f"{wf_user_directory}/{deployment}/exp1/plots/"
        plots = os.listdir(plots_dir)
        for p in plots:
            print(p)
            if 'timeline' in p :
                full_path = f"{plots_dir}/{p}"
                copy_pdf_file(full_path,timeline_dir)
        print(log_file_path)
        logs = read_log_file(log_file_path)
        dist_dict = init_dict(logs)
        node_execs = dist_dict['functions']
        lstt = node_execs["1"]
        god_list.append(lstt)
        i += 1

    plot_violin(god_list)




