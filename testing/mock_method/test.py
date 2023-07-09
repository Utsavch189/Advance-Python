import requests
import unittest
from unittest import TestCase
from unittest.mock import Mock,patch

BASE_URL='https://todo.pixegami.io'

def create_task():
    url=BASE_URL+'/create-task'
    data={
        "content": "hey",
        "user_id": "134",
        "task_id": "t134",
        "is_done": False
    }
    res=requests.put(url=url,json=data)
    return res.status_code

class Test(TestCase):

    @patch('requests.put')
    def test_create_task(self,mock_get):
        mock_res=Mock()
        expected_res_status=200
        mock_res.json.status_code.return_value=expected_res_status

        mock_get.return_value=mock_res

        createTask=create_task()
        self.assertEqual(createTask,expected_res_status)

if __name__=='__main__':
    unittest.main()