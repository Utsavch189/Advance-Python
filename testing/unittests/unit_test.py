import requests
import unittest
from unittest import TestCase


BASE_URL='https://dummyjson.com/products'

def get_data(ids):
    url=BASE_URL+f'/{ids}'
    res=requests.get(url)
    return res

class MyTest(TestCase):

    def test_api(self):
        expected_res={"id":1,"title":"iPhone 9","description":"An apple mobile which is nothing like apple","price":549,"discountPercentage":12.96,"rating":4.69,"stock":94,"brand":"Apple","category":"smartphones","thumbnail":"https://i.dummyjson.com/data/products/1/thumbnail.jpg","images":["https://i.dummyjson.com/data/products/1/1.jpg","https://i.dummyjson.com/data/products/1/2.jpg","https://i.dummyjson.com/data/products/1/3.jpg","https://i.dummyjson.com/data/products/1/4.jpg","https://i.dummyjson.com/data/products/1/thumbnail.jpg"]}
        expected_status=200
        actual_res=get_data(1)
        self.assertEqual(expected_res,actual_res.json())
        self.assertEqual(expected_status,actual_res.status_code)



if __name__=='__main__':
    unittest.main()
