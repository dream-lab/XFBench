### Description of function

The sine of the numbers within the range of 'seed' is computed repeatedly 'req' times, and the time taken to compute the same is returned

### Description of Input JSON Params

         seed (Integer): Range of numbers, whose sine is computed.
         req (Integer): Number of times (iterations) the sine of the 'seed' is computed.

### Description of Output JSON Params

         Response (String): The latency of this function is returned.

### Sample Input JSON

 ```json
 {
    "seed": 300,
    "req": 300
}
 ```

 ### Sample Output JSON

 ```json
 {
    "message": "Success",
    "result": {
        "body": {
            "Response": "Total time to execute the function is: 0.12358665466308594 seconds"
        },
        "metadata": null,
        "statusCode": 200
    },
    "statusCode": 200
}
 ```

### Dependencies

    Python 3.10.6

### Citations 

    Kaustubh Rajendra Rajput, Chinmay Dilip Kulkarni, Byungjin Cho, Wei Wang, and In Kee Kim, "EdgeFaaSBench: Benchmarking Edge Devices Using Serverless Computing," In 2022 IEEE Internatinoal Conference on Edge Computing (EDGE), Barcelona Spain, July, 2022

    [@EdgeFaaSBench](https://github.com/kaustubhrajput46/EdgeFaaSBench/tree/main)

### Authors


- Jahnavi Murali [@jahnavimurali](https://www.github.com/jahnavimurali)
- Harini Mohan [@HariniMohan2110875](https://www.github.com/HariniMohan2110875)


