import requests
import unittest
from unittest import TestCase
from unittest.mock import Mock,patch

"""
https://docs.python.org/3/library/unittest.mock-examples.html#mock-patching-methods
"""

BASE_URL='https://dummyjson.com/products'

def get_data(ids):
    url=BASE_URL+f'/{ids}'
    res=requests.get(url=url)
    return res.json()

class Test(TestCase):

    @patch('requests.get')
    def test_get_data(self,mock_get):
        mock_res=Mock()
        expected_res={"id":1,"title":"iPhone 9","description":"An apple mobile which is nothing like apple","price":549,"discountPercentage":12.96,"rating":4.69,"stock":94,"brand":"Apple","category":"smartphones","thumbnail":"https://i.dummyjson.com/data/products/1/thumbnail.jpg","images":["https://i.dummyjson.com/data/products/1/1.jpg","https://i.dummyjson.com/data/products/1/2.jpg","https://i.dummyjson.com/data/products/1/3.jpg","https://i.dummyjson.com/data/products/1/4.jpg","https://i.dummyjson.com/data/products/1/thumbnail.jpg"]}

        mock_res.json.return_value=expected_res

        mock_get.return_value=mock_res

        getData=get_data(1)

        self.assertEqual(getData,expected_res)

if __name__=='__main__':
    unittest.main()