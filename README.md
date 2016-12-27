# CF 401 - Python HTTP-Server Assignment

The goal of this assignment was to write a basic but functional HTTP server.

#Summary

The assignment was to implement a simple HTTP Server with concurrency.  A user should be able to send a formatted GET request through the client via the command line and receive a formatted response from the server.  The server is able to return requests for text files, images (as byte strings), or directories.  If the the GET request is improperly formatted or requests an unvailable or forbidden resource, the server will return a relevant error as a properly formatted HTTP response.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/http_server_final.html



# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | 
| -----------------------  | ----- | ---- | ----- | 
| client.py                |  25   |  1   |  96%  | 
| server.py                |  97   |  42  |  67%  | 
| test_server.py           |  35   |  0   |  100% |     
| -----------------------  |  ---  |  --  | ----  | 
| TOTAL                    |  157  |  43  |  78%  | 



# Comments about implementation:
 * Besides implementing gevent, major changes from step3 are refactoring the resolve_uri and parse_request function to return specific error codes in the event of some sort of error.  Additionally, we implemented a dictionary in the response_err function to hold the requried information for returning various HTTP error responses based on relevant error codes.

