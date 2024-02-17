# XFBench: A Cross-Cloud Benchmark Suite for Evaluating FaaS Workflow Platforms
Functions-as-a-Service (FaaS) is a widely used serverless computing abstraction that helps developers build applications using event-driven, stateless functions that execute on the cloud. Commercial FaaS platforms like AWS Lambda and Azure Functions offer elastic auto-scaling and invocation-level billing to ease operations. Applications are often composed as a dataflow of FaaS functions that are orchestrated by FaaS workflow platforms like AWS Step Functions or Azure Durable Functions. However, the proprietary nature of FaaS platforms on public clouds means that their internals are less understood. While benchmarks to characterize FaaS platforms exist, none are available for a principled evaluation of FaaS workflow platforms. Further, they are less configurable, and often limited to simple workloads and a single cloud provider. We address this by proposing XFBench, an end-to-end automated benchmarking framework for FaaS workflows, and an accompanying function, workflow and workload suite. The user provides a generic definition of the workflow and workload for benchmarking, and XFBench automatically deploys the workflows across multiple cloud platforms, generates client requests, and profiles the execution. We evaluate XFBench with realistic workflows and workloads on AWS and Azure platforms in different global regions to understand inter-function communication, function execution time, and cold start scaling and offer unique insights.

## Cite this work as
* V. Kulkarni, N. Reddy, T. Khare, H. Mohan, J. Murali, Mohith A, Ragul B, S Balajee, Sanjjit S, Swathika, Vaishnavi S, Yashasvee, C. Babu, A. S. Prasad and Y. Simmhan, "XFaaS: Cross-platform Orchestration of FaaS Workflows on Hybrid Clouds," 2024 IEEE/ACM 24th International Symposium on Cluster, Cloud and Internet Computing (CCGrid), Philadephia, Pennsylvania, 2024

## Acknowledgement
*This research was performed as part of the IBM IISc Hybrid Cloud Lab, an open research collaboration jointly between the DREAM:Lab at IISc and researchers at IBM India Research Lab, Bangalore.*

## License and Copyright
This code is released under Apache License, Version 2.0
https://www.apache.org/licenses/LICENSE-2.0.txt

Copyright (c) 2024 DREAM:Lab, Indian Institute of Science. All rights reserved.