# CF 401 - Python HTTP-Server Assignment

The goal of this assignment was to write a basic but functional HTTP server.

#Summary

The goal was to create a functioning HTTP server and client.  A user should be able to send a formatted GET request through the client via the command line and receive a formatted response from the server.  The server is able to return requests for text files, images (as byte strings), or directories.  If the the GET request is improperly formatted or requests an unvailable or forbidden resource, the server will return a relevant error as a properly formatted HTTP response.


For more information on the assignment, see here: https://codefellows.github.io/sea-python-401d5/assignments/http_server_3.html



# Coverage for Step3:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover | 
| -----------------------  | ----- | ---- | ----- | 
| client.py                |  23   |  1   |  96%  | 
| server.py                |  106  |  37  |  65%  | 
| test_server.py           |  43   |  0   |  100% |     
| -----------------------  |  ---  |  --  | ----  | 
| TOTAL                    |  172  |  43  |  78%  | 


# Comments for Implementation:
    * A more robust error handling system was implemented, the user can now receive appropriate HTTP errors.
    * Responses have been properly formatted to allow rendering in a web browser.
    * The server is now able to handle the odd cases where requests from the client escape all newline characters.
    
