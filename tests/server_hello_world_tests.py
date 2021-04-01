import unittest
import requests
from bs4 import BeautifulSoup


# The following tests are all integration tests and thus require the server_hello_world.py file to have been executed
# before running these tests.
class ServerHelloWorldTests(unittest.TestCase):

    # CHeck that 200 status code is returned for a GET request
    def test_server_response_status_code_is_ok_for_GET_request(self):
        response = requests.get("http://localhost:8080")
        self.assertEqual(200,response.status_code)

    def test_title_should_be_correctly_populated_for_GET_request(self):
        response = requests.get("http://localhost:8080")
        html_content = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual("Hello World example", html_content.find_all('title')[0].text)

    def test_body_message_should_be_correctly_populated_for_GET_request(self):
        response = requests.get("http://localhost:8080")
        html_content = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual("Hello World!", html_content.find_all('p')[0].text)

    def test_server_response_status_code_is_server_error_for_POST_request(self):
        response = requests.post("http://localhost:8080", [("name", "wibble")])
        self.assertEqual(501,response.status_code)

    def test_title_should_be_correctly_populated_for_POST_request(self):
        response = requests.post("http://localhost:8080", [("name", "wibble")])
        html_content = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual("Error response", html_content.find_all('title')[0].text)

    def test_body_should_be_correctly_populated_for_POST_request(self):
        response = requests.post("http://localhost:8080", [("name", "wibble")])
        html_content = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual("Error code: 501",
                         html_content.find_all('p')[0].text)
        self.assertEqual("Message: Post requests are not permitted.",
                         html_content.find_all('p')[1].text)
        self.assertEqual("Error code explanation: 501 - Server does not support this operation.",
                         html_content.find_all('p')[2].text)


if __name__ == '__main__':
    unittest.main()
