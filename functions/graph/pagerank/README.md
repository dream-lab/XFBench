# Pagerank

## Description of function
The graph pagerank benchmark calculates the process time for a pagerank 

## Description for input params 
This function takes in the graph and also the graph generation time in the form of a dictionary

## Description for output params
The generated pagerank and its corresponding process time is calculated and returned

## Sample input json

```json
{
    "output":graph,
    "graph_time":graph_generating_time  
}
```

## Sample output json

```json
{
    "message": "Success",
    "result": {
        "body": {
            "return": {
                "measurement": {
                    "compute_time": 1144.0,
                    "graph_generating_time": 458873.0
                },
                "result": 0.1
            }
        },
        "metadata": null,
        "statusCode": 200
    },
    "statusCode": 200
}
```
## Dependencies
python3 3.10.12

datetime

igraph

## Citation to external sources:

SeBS: a serverless benchmark suite for function-as-a-service computing [@pdf](https://dl.acm.org/doi/abs/10.1145/3464298.3476133)

Workflows - 
[@Serverless Benchmarks](https://github.com/spcl/serverless-benchmarks/tree/master)

XFaaS -
[@xfaas-workloads](https://github.com/dream-lab/xfaas-workloads) 

## Authors

Mohith A - [@mohithadluru](https://github.com/mohithadluru)

Sanjjit S - [@sanjjit001](https://github.com/sanjjit001)
