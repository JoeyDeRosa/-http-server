# CF 401 - Python HTTP-Server Assignment

The goal of this assignment was to write a basic but functional HTTP server.

#Summary

The assignment was to implement a simple HTTP Server.  A user should be able to send a formatted GET request through the client via the command line and receive a formatted response from the server.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/http_server_2.html



# Coverage for step2:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | 
| -----------------------  | ----- | ---- | ----- | 
| client.py                |  23   |  1   |  96%  | 
| server.py                |  78   |  50  |  36%  | 
| test_server.py           |  15   |  0   |  100% |     
| -----------------------  |  ---  |  --  | ----  | 
| TOTAL                    |  116  |  51  |  56%  | 



# Comments about implementation:
    * For step2, the goal was to create a properly formatted HTTP response to a properly formatted HTTP request.
    * parse_request() in this implementation accepts a string as input, parses the string to look for the required components of request and returns either the URI or a '400' error code.
    * After this step, the sever will pass the response to either response_err or response_ok to generate a properly formatted HTTP response.
