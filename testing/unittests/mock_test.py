import requests
import unittest
from unittest import TestCase
import json
from unittest.mock import Mock,patch
  
"""
Consider yourself developing software that needs an external API as a dependency and while testing we found that the API is not functional for some reason. 
As we know testing is one of the most critical phases in SDLC (Software Development Life Cycle) and without the API dependency, 
testing could not be performed. We have a few solutions like waiting for the API to become functional or making our own API.

Now both of the solutions are very time and resource consuming which could be disastrous for an organization if there could be a way to mimic the behaviour of the API without using the actual API now when mocking API can be used.

Here when mocking external services could be a better solution in this we make a mock which is a fake object that we construct to look and act like the real one. 
We swap the actual object with a mock and trick the software into thinking that the mock is real. 
By this developers can test the software or code without relying on the external service, 
especially when the external services are down.
"""

"""
Developers can make a fake mock object that mimics the behaviour of 
a real object and perform the testing of the code in an isolated environment.
"""

# get_data() is a function that makes a request to an external api and returns the data in json format
def get_data():
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    return response.json()



# TestGetData is a class that contains a test_get_data() 
# method that tests the get_data() function using the mock library
  
class TestGetData(TestCase):
    @patch('requests.get')
    def test_get_data(self, mock_get_data):
        """
        Test that get_data() returns the correct data 
        demonstrating the use of the mock library
        """
  
        mock_data = {'userId': 1, 'id': 1,
                     'title': 'delectus aut autem', 'completed': False}
  
        mock_get_data.return_value = Mock()
  
        mock_get_data.return_value.json.return_value = mock_data
        mock_get_data.return_value.status_code = 200
  
        result = get_data()
  
        self.assertEqual(result, mock_data)
    
if __name__ == '__main__':
    unittest.main()