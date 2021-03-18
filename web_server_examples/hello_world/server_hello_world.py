
# Need to import these two classes to allow handling of a request and establish a local server.
from http.server import BaseHTTPRequestHandler, HTTPServer

# Server intended to be local only, so set hostname accordingly.
hostName = "localhost"
# Set the server port value
serverPort = 8080


# Define the server class to inherit from BaseHTTPRequestHandler.
class HelloWorldServer(BaseHTTPRequestHandler):
    # Define a method to generate and write a response
    #  Override do_GET to handle a GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World example</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Hello World!</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    # Override do_POST to handle a POST request being made in error.
    def do_POST(self):
        self.send_error(501, "Post requests are not permitted")


# Initialise a HTTPServer instance using the defined host name, server port and defined server class.
# When started, the server will run until the user enters keyboard input into the console window running this example
# file.  At that point, the web server is shut down.
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), HelloWorldServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    # Run the server forever until keyboard input interrupts.
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Shut down the web server.
    webServer.server_close()
    print("Server stopped.")
