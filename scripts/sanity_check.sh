#!/bin/bash

python3 bin/serwo/xfbench_run.py \
--csp aws \
--region us-east-1 \
--max-rps 1 \
--duration 10 \
--payload-size small \
--dynamism static \
--wf-name graph \
--wf-user-directory /XFBench/workflows/custom_workflows/graph_processing_wf \
--dag-file-name dag.json \
--teardown-flag 0 \
--client-key localhost

sleep 10

python3 bin/serwo/xfbench_run.py \
--csp azure \
--region eastus \
--max-rps 1 \
--duration 10 \
--payload-size small \
--dynamism static \
--wf-name graph \
--wf-user-directory /XFBench/workflows/custom_workflows/graph_processing_wf \
--dag-file-name dag.json \
--teardown-flag 0 \
--client-key localhost

python3 /XFBench/scripts/confirm_sanity_check.py \
--wf-user-directory /XFBench/workflows/custom_workflows/graph_processing_wf 



> /XFBench/deployments.txt