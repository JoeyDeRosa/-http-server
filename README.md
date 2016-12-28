# CF 401 - Python HTTP-Server Assignment

The goal of this assignment was to write a basic but functional HTTP server.

#Summary

The assignment was to implement a simple HTTP Server.  A user should be able to send a formatted GET request through the client via the command line and receive a formatted response from the server.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/http_server_final.html



# Coverage for echo:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | 
| -----------------------  | ----- | ---- | ----- | 
| client.py                |  29   |  1   |  97%  | 
| server.py                |  30   |  30  |  0%   | 
| test_server.py           |  9    |  0   |  100% |     
| -----------------------  |  ---  |  --  | ----  | 
| TOTAL                    |  65   |  31  |  52%  | 



# Comments about implementation:
    * For the echo assignment, the goal was to write a server to echo any message sent from a client.
    * The echo should work for messages of any size and containing any characters (e.g. non-ASCII characters)
