#SERVER HELLO WORLD

This is a "Hello World" example extending the BaseHttpRequestHandler to receive a GET request and return a "Hello World!"
 HTML string. This simple example also returns an error message should a POST request be received.

The GET request is handled via overriding the do_GET method in BaseHttpRequestHandler.  This builds a simple response 
containing the "Hello World" method with a HTTP code of 200 to indicate the request executed correctly. 

The POST request overrides the do_POST method in BaseHttpRequestHandler.

Python tests have been created within the **server_hello_world_tests.py** file.
##USAGE
###CURL
From a console window, execute the following commands :- 
* curl http://localhost:8080 to execute a GET request
* curl -d "name=wibble" http://localhost:8080 to execute a POST request
####EXPECTED OUTPUT
#####GET REQUEST
        <html>
            <head>
 	             <title>Hello World example</title>
            </head>
            <body>
 	             <p>Hello World!</p>
            </body>
        </html>
#####POST REQUEST    
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
                <title>Error response</title>
            </head>
            <body>
                <h1>Error response</h1>
                <p>Error code: 501</p>
                <p>Message: Post requests are not permitted.</p>
                <p>Error code explanation: 501 - Server does not support this operation.</p>
            </body>
        </html>
###POSTMAN
A collection in this directory, **Python Simple Hello World Example Tests.postman_collection.json**, has been created with automated tests for this example.  Run the server application and then
run the test collection from within postman.


