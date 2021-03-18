# wcl-basic-python
This project is intended to be used to increase knowledge about Python.

Examples will be placed within separate directories and added here as and when.

All examples have been edited and run in PyCharm Community edition.
# Examples
Examples are described below, under the directory they are stored in.
## web_server_examples
###hello_world
A simple example of a "Hello World" application.  Default Python libraries are used to instantiate a web server that
provides a url on http://localhost:8080/.
A GET request to that URL, when the server file is running, has HTML returned with "Hello World!" as a
cheery message.
When a POST request is sent to that URL, then an Error response is returned instead of being friendly.

The example contains a POSTMAN collection of tests for this example along with Python tests against the created server
example.

|File|Description|
|:---|:---|
|server_hello_world.py|Example "Hello World" app via built in server|
|server_hello_world_tests.py|Integration tests for the "Hello World" example|
|Hello World Postman Tests.json|Collection of Postman tests for the "Hello World" app.|
