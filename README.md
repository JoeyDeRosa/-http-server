# CF 401 - Python HTTP-Server Assignment

The goal of this assignment was to write a basic but functional HTTP server.

#Summary

The assignment was to implement a simple HTTP Server.  A user should be able to send a formatted GET request through the client via the command line and receive a formatted response from the server.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/http_server_final.html



# Coverage for step1:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | 
| -----------------------  | ----- | ---- | ----- | 
| client.py                |  28   |  2   |  93%  | 
| server.py                |  44   |  36  |  18%  | 
| test_server.py           |  9    |  0   |  100% |     
| -----------------------  |  ---  |  --  | ----  | 
| TOTAL                    |  81   |  38  |  53%  | 



# Comments about implementation:
    * For step1, the goal was to implement the ability to send back to the client a properly formatted HTTP 200 response while logging the sent message on the server side.
    * Messages should be able to include non-ASCII characters and be of any size (e.g. a factor of the buffer length).
