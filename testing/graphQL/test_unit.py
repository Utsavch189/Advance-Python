############# GET ##################
import requests
import unittest
from unittest import TestCase
from unittest.mock import Mock,patch

body="""
   { 
        allFiles{
            user,
            filename
        }
    }
"""
def get_data():
    url='http://127.0.0.1:8000/app/get'
    data=requests.get(url=url,json={'query':body})
    return data

class Test(TestCase):

    
    def test_get_data(self):
        
        expected_res={'data': {'allFiles': [{'user': 'iyahamis', 'filename': 'a.txt'}, {'user': 'csvfgs', 'filename': 'uqw.jpeg'}, {'user': 'uts', 'filename': 'harry potter2.jpg'}]}}
        expected_status_code=200
        actual_data=get_data()

        self.assertEqual(actual_data.json(),expected_res)
        self.assertEqual(actual_data.status_code,expected_status_code)

#if __name__=='__main__':
#    unittest.main()

############# update ##################

body2="""
  mutation abc{
    update(filename:"harry2.jpg",user:"uts"){
      updates{
        filename,
        user
      }
    }   
}
"""
def update_data():
    url='http://127.0.0.1:8000/app/post'
    data=requests.post(url=url,json={'query':body2})
    return data


class Test(TestCase):

    
    def test_get_data(self):
        expected_res={'data': {'update': {'updates': {'filename': 'harry2.jpg', 'user': 'uts'}}}}
        expected_status_code=200
        actual_data=update_data()

        self.assertEqual(actual_data.json(),expected_res)
        self.assertEqual(actual_data.status_code,expected_status_code)

if __name__=='__main__':
    unittest.main()