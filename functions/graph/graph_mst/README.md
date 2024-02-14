### Description of function

Given a graph, its minimum spanning tree is constructed.

### Description of Input JSON Params

           graph (iGraph object): Graph (given its size) generated in a prefix function is sent as an igraph object.
           measurement(graph-generating time) (Double precision floating point number): Graph generation (Prefix function) Latency.

### Description of Output JSON Params

           result (Number): Part of the minimum spanning tree constructed
           measurement(graph-generating time) (Double precision floating point number): Graph generation (Prefix function) Latency.
           measurement(compute time) (Double precision floating point number): MST construction Latency.

### Sample Input JSON

 ```json
{
    "graph": "<igraph.Graph object at 0x7fe64f7dd740>", 
"measurement": {"graph_generating_time": 2345.0}
}
 ```

 ### Sample Output JSON

 ```json
 {
    "message": "Success",
    "result": {
        "body": {
            "measurement": {
                "compute_time": 311.0,
                "graph_generating_time": 2345.0
            },
            "result": 0
        },
        "metadata": null,
        "statusCode": 200
    },
    "statusCode": 200
}
 ```

### Dependencies

    Python 3.10.6
    igraph 0.10.6

### Citations 

   - [Serverless Benchmarks](https://github.com/spcl/serverless-benchmarks)
   - [SeBS: a serverless benchmark suite for function-as-a-service computing](https://dl.acm.org/doi/abs/10.1145/3464298.3476133)
 

### Authors


- Jahnavi Murali [@jahnavimurali](https://www.github.com/jahnavimurali)
- Harini Mohan [@HariniMohan2110875](https://www.github.com/HariniMohan2110875)


