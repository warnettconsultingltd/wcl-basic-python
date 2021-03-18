# wcl-basic-python

This project is intended to be used to increase knowledge about Python.

Examples will be placed within separate directories and added here as and when.

All examples have been edited and run in PyCharm Community edition.

# Examples

Examples are described below, under the directory they are stored in.

## basic_language_structures
|File|Description|
|:---|:---|
|basic_comments.py|Sample "code" displaying different comment types.|
|basic_data_types.py|Sample code displaying basic Python Number and String data types.|
|basic_input.py|Sample code to input a username and display a Hello message using the input name.|
|basic_logical_expressions.py|Sample code showing logical expressions and operators.|
|basic_numbers.py|Sample  code showing basic numeric operations.|
|list_data_type.py|Sample code showing the list data type.|

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
