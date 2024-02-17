# XFBench: A Cross-Cloud Benchmark Suite for Evaluating FaaS Workflow Platforms
##### ***V. Kulkarni<sup>1</sup> , N. Reddy<sup>1</sup> , Tuhin Khare<sup>1</sup> , H. Mohan<sup>3</sup> , J. Murali<sup>3</sup> , Mohith A<sup>3</sup> , Ragul B<sup>3</sup> , S. Balajee<sup>3</sup> , Sanjjit S<sup>3</sup>, Swathika<sup>3</sup> , Vaishnavi S<sup>3</sup> , Yashasvee<sup>3</sup> , C. Babu<sup>3</sup> , A. S. Prasad<sup>2</sup> and Y. Simmhan<sup>1</sup>***

<sup>1</sup> Indian Institute of Science, India ; <sup>2</sup> IIT, Ropar, India ; <sup>3</sup> SSN College of Engineering, India

{varadk, simmhan}@iisc.ac.in,   abhinandansp@iitrpr.ac.in,  chitra@ssn.edu.in

### I. *Introduction*

XFBench is a multi-cloud benchmarking framework to evaluate FaaS workflow platforms of public/ private cloudvproviders such as AWS Lambda, Azure Function, etc. It offers:

- ***Diverse and extensible function and workflow benchmarks*** with a suite of serverless functions that are also composed into meaningful workflows. Users can also add new functions and compose new workflows.

- ***A benchmarking framework that is Cloud Service Provider (CSP) agnostic***, enabled through the use of the XFaaS platform that allows multi-cloud deployment of FaaS workflows. Currently, it supports AWS and Azure public clouds
  
- ***Zero-touch workload generation and reporting*** where users can configure and vary the workload parameters such as payload size, request rate and rate variability to generate workloads for the deployed workflows being benchmarked.

We vary these workloads to help understand the behaviour of different CSPs for FaaS workflows. This artifact evaluation proposes to meet the requirements of **Results Reproduced (ROR-R)**. Our instructions are designed to help reproduce the benchmarking behavior of XFBench on AWS and Azure clouds, and reproduce the central results and claims in the main paper, as described below. The GitHub repository for the XFBench benchmark framework source code is at https://github.com/dream-lab/XFBench/tree/CCGRID2024. XFBench also depends on the XFaaS platform used for FaaS workflow deployment, available at https://github.com/dream-lab/XFaaS/tree/CCGRID2024. These have also been archived as *Open Research Objects (ORO)* at Zenodo with DOI: https://zenodo.org/records/10673612. The credentials required to run the workloads on AWS and Azure clouds have been emailed to the AE Chairs. We recommend that the AE evaluators follow the detailed instructions available in the XFBench GitHub page that go beyond this Appendix.

### II. ***Configuring and Running XFBench***
We first establish that the artifacts are *Reusable Research Objects (ROR)* by providing the documentation to deploy and run XFBench in a functional manner that promotes reusability.

#### *A. XFaas and XFBench Setup*

**Estimated Time:** 30 mins

**Pre-requisites:** A Linux desktop with Internet connection. Credentials to AWS and Azure.

We provide a docker container with all the dependencies installed in the repo. Line 1 below first clone the public github repository of XFaaS that contains a Dockerfile that contains all the base dependencies. Lines 2–3 build and run the Docker container. Line 4 brings you inside thebashshell of the container. Lines 6–8 set up thecloud credentials in the container, which have been shared with the AE Chairs. Lines 8–9 will clone theCCGRID2024branch of XFaaS and XFBench repos into the container. Lines 10–11 set the absolute path of the two repos as an environment variable. Finally, Line 12–13 install all the Python dependencies. The XFBench setup is complete.

```shell
1 git clone -b CCGRID2024 https://github.com/dream-lab/XFaaS.git
2 cd XFaaS
3 docker build -t xfaas:1..
4 docker run -d --name xfaas-container xfaas:1.
5 docker exec -it xfaas-container bash
6 %% We are inside the bash shell of the container
7 az login -u <username> -p <password>
8 export AZURE_SUBSCRIPTION_ID=<Azure account subscription id>
9 aws configure
10 git clone -b CCGRID2024 https://github.com/dream-lab/XFaaS.git
11 git clone -b CCGRID2024 https://github.com/dream-lab/XFBench.git
12 cp -r XFaaS/serwo /XFBench/bin/
13 export XFBENCH_DIR=/XFBench
14 export XFAAS_DIR=/XFaaS
15 cd XFBench
16 pip3 install -r requirements.txt
```

#### *B. Running XFBench*
Before running these commands, you must be in the `bash` shell of the above container and in the `XFBench` folder.
```shell
1 docker exec -it xfaas-container bash
2 cd XFBench
```

The `bin/serwo/xfbench_run.py` command-line is used to *deploy a workflow* and *run a workload* using XFBench.

```shell
1 python3 bin/xfbench_run.py
2 --csp <cloud provider> --region <region>
3 --max-rps <rps> --duration <duration(s)>
4 --payload-size <size>
5 --dynamism <dynamism pattern>
6 --wf-name <workflow name>
7 --path-to-client-config <path to VM config if running experiments from a VM>
8 --dag-file-name <filename>
9 --teardown-flag <delete flag for remote application>
10 --client-key <client-id / localhost (if local)>
11 --wf-user-directory <absolute path to user workflow>
```

#### *Sanity Check*
**Estimated Time:** 10 mins
A sample script `scripts/sanity_check.sh` can be used to verify the correctness using a simple workload that runs the graph workflow for **10 seconds** using a small payload at **1 RPS**?. ****TODO Yogesh: What is the output expected? How do they know it ran properly? Post-condition?**
```shell
1 ./scripts/sanity_check.sh
```
**TODO Yogesh: do we automatically cleanup the workflow deploy-
ment?****

### III. ***Reproducing XFBench Results***

We reproduce 5 key claims from the paper. To balance coverage, brevity and monetary cost, we validate a large and representative subset of our experiments to establish these claims. Specifically, we use the *Graph Workflow* on the US region(East USA/North Virginia) of *AWS* and *Azure*. We vary three workload dimensions to analyze their responses: *Payload Size* (Small/Medium/Large),   *Requests per Second* (RPS; 1, 4, 8 rps), and *Request Rate Dynamism* (Step, Sawtooth and Alibaba). We also evaluate *cold starts* and *scaling behavior* using a gentle step and a growing step. These reproduce results from § V-C and § V-E (subset of Figs. 5–10) in the paper, and **TODO cost≈US$???** for a single run. For brevity, we omit § V-B which are just micro-benchmarks, temporal behavior runs in § V-D which take 24 hours each, and the contrast with other regions (Southeast-Asia, SEA) and workflows (Text, Image).

We've provided 5 scripts that each run one of the experiments with the relevant `xfbench_run.py` parameters, and then invoke the `xfbench_plot.py` script of the logs to plot the results similar to the figures from the main paper.

**Common Pre-requisites:** A running XFaaS container and confirmed sanity check from § II.

***A. Claim 1: Effect of Variation in Payload Sizes***

**Estimated Time:** 50 mins

We reproduce the results from § V-C (payload size variability). The key claim is that the *inter-function communication times increase with an increase in payload size*. Executing the command below will invoke the graph workflow on AWS and Azure with diverse payload sizes at a static 1 RPS. The relevant plot is in Fig. 5a. After running this experiment, a similar plot should be auto-generated in `plots/payload_variation.pdf`.
```
1 ./scripts/run_payload_variation_experiments.sh
```

***B. Claim 2: Effect of Variation In Requests Rate***

**Estimated Time:** 60 mins

We reproduce the results from § V-C (RPS variability). The key claim is that the *inter-function communication time and hence end-to-end (E2E) time increase sharply for Azure, while the E2E time remains stable for AWS when the RPS increases, denoting poor rate-scaling for Azure*. Running the script invokes the graph workflow in AWS and Azure with variation in RPS using a medium payload size. The plots from the runs will be placed in `plots/rps_variation.pdf`, and should be similar to Fig. 6b.
```
1 ./scripts/run_rps_variation_experiments.sh
```

***C. Claim 3: Effect of Dynamism in Request Rate***

**Estimated Time:** 90 mins
We reproduce the results from § V-C (dynamic RPS). The key claim is thatAWS adapts to incoming request rate variability quickly as compared to Azure, which is unstable. Running the script below will vary the dynamism of the request rate for the graph workflow using step, sawtooth and Alibaba distributions, using a medium payload. The relevant plot is Fig. 6c and Fig. 7. After running this experiment, a similar plot as Fig. 6c should be auto-generated in `plots/dynamism_variation.pdf`. To enhance the readability, we split Figs. 7 into separate plots for AWS and Azure for each rate-dynamism and place the timeline plots in `plots/dynamism_timelines`.

```
1 ./scripts/run_dynamism_variation_experiments.sh
```

***D. Claim 4: Coldstart Behaviour***

**Estimated Time:** 140 mins

Here, we reproduce results from § V-E(1) examining cold starts, with the observation thatboth *AWS and Azure have a cold start overhead as seen from higher E2E times when invoking the workflows after a pause*. The script below runs the a *gentle-step* workload (1 RPS execution, sleep for 5 mins, repeat 10 times) on a singleton workflow having the PageRank function. The relevant plots in the paper are Figs. 9a and 9b, which are together reproduced as a single plot after the execution of this script under `/plots/gentle_step_violin.pdf`.

```
1 ./scripts/run_gentle_step.sh
```

***E. Claim 5: Scaling Behaviour***

**Estimated Time:** 80 mins

Lastly, we reproduce the scaling behaviors of the CSPs as described in § V-E, where we claim that *AWS is very stable and extremely good at scaling, while Azure exhibits poor scaling and becomes unstable at high rps load*. The script below executes a growing step workload (RPS increases exponentially from 1–128) on the PageRank singleton workflow. The results are shown in Fig. 10 of the paper, and reproduced under `plots/growing_step_timelines/` after the script finishes.


```
1 ./scripts/run_growing_step.sh
```
**TODO Yogesh: how about Fig 8(b)?**
