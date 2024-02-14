# Floating Point Cosine - Micro

## Description of function
Single node function: Calculates the cosine value of 'req' degrees for 'seed' number of times

## Description for input params 
req (int): Number of iterations
seed (int): Value of the cosine angle

## Description for output params
int: time taken to execute the function

## Sample input json

```json
{
    "req":180,
    "seed":120
}
```

## Sample output json

```json
{
    "message": "Success",
    "result": {
        "body": "Latency : 0.0037086009979248047 seconds",
        "metadata": null,
        "statusCode": 200
    },
    "statusCode": 200
}
```
## Dependencies
python3 3.10.12

Math

Time

## Citation to external sources:

[@EdgeFaaSBench: Benchmarking Edge Devices Using Serverless Computing](https://wwang.github.io/papers/EdgeFaaSBench.pdf)

Workflows - 
[@EdgeFaaSBench](https://github.com/kaustubhrajput46/EdgeFaaSBench/tree/main)

XFaaS -
[@xfaas-workloads](https://github.com/dream-lab/xfaas-workloads) 

## Authors

Mohith A - [@mohithadluru](https://github.com/mohithadluru)

Sanjjit S - [@sanjjit001](https://github.com/sanjjit001)
