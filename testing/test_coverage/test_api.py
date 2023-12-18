import unittest
from api import API

class TestAPI(unittest.TestCase):
    
    def test_wrong_request_body(self):
        with self.assertRaises(Exception):
            api=API({
                "users":"utsav"
            })
            api.get_userFromRequest()
        
    def test_wrong_user(self):
        with self.assertRaises(Exception):
            api=API({
                "user":"antick"
            })
            api.get_userFromRecord()
    
    def test_get_userFromRequest_return_data(self):
            api=API({
                "user":"utsav"
            })
            _data=api.get_userFromRequest()
            _data_to_be_expected="utsav"
            self.assertEqual(first=_data,second=_data_to_be_expected,msg="returned data from request body is not matching!")
    
    def test_get_userFromRecord_return_data(self):
            api=API({
                "user":"utsav"
            })
            _data=api.get_userFromRecord()
            _data_to_be_expected={
                "age":22,
                "address":"Muragacha",
                "DOB":"11-02-2001"
            }
            self.assertEqual(first=_data,second=_data_to_be_expected,msg="returned data from record is not matching!")
