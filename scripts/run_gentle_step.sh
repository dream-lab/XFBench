#!/bin/bash

python3 bin/serwo/xfaas_run_benchmark.py \
--csp aws \
--region us-east-1 \
--max-rps 1 \
--duration 3700 \
--payload-size medium \
--dynamism gentle-step \
--wf-name pagerank \
--wf-user-directory /XFBench/workflows/singleton_workflows/graph/pagerank \
--dag-file-name dag.json \
--teardown-flag 0 \
--client-key localhost \
--is_singleton_wf 1 \
--function-class graph \
--function-name pagerank \
--function-code PGRK \
--node_name pagerank

echo "AWS Gentle Step Done!!"
sleep 10

python3 bin/serwo/xfaas_run_benchmark.py \
--csp azure \
--region eastus \
--max-rps 1 \
--duration 3700 \
--payload-size medium \
--dynamism gentle-step \
--wf-name pagerank \
--wf-user-directory /XFBench/workflows/singleton_workflows/graph/pagerank \
--dag-file-name dag.json \
--teardown-flag 0 \
--client-key localhost \
--is_singleton_wf 1 \
--function-class graph \
--function-name pagerank \
--function-code PGRK \
--node_name pagerank

echo "AZURE Gentle Step Done!!"
sleep 10

python3 plots/plot_gentle_step.py \
--wf-user-directory /XFBench/workflows/singleton_workflows/graph/pagerank

echo "Plotting Done!!"

> /XFBench/deployments.txt