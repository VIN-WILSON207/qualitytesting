# my_unittest.py # Import necessary modules
import unittest   # Imports the Python unit testing framework
from app import app   # Imports the Flask app from your app.py file


class TestApp(unittest.TestCase):   # Creates a test class that inherits from unittest.TestCase
    def setUp(self):                  # This method runs before each test case
        self.app = app.test_client()    # Creates a test client for your Flask application

    def test_home_route(self):          # Test method for the home route ('/')
        response = self.app.get('/')       # Makes a GET request to the root URL ('/')
        self.assertEqual(response.status_code, 200)     # Asserts that the HTTP status code is 200 (OK)
         # Asserts that the JSON response matches the expected message
        self.assertEqual(
            response.json, 
            {"message": "Hello level 400 FET, Quality Assurance!"})

# This block runs the tests when the file is executed directly
if __name__ == '__main__':
    unittest.main()
