
"""
https://www.wwt.com/article/rest-api-integration-testing-using-python
"""
"""
1. pytest --> test all python files of that dir where names of files are started with test_
2. pytest test_abc.py
3. pytest -v
4. pytest -sv --html report.html
5. pytest -s --> able to print() in testing
"""


BASE_URL='https://todo.pixegami.io'

import requests
from jsonschema import validate

def test_create_task():
    url=BASE_URL+'/create-task'
    data={
        "content": "hey",
        "user_id": "134",
        "task_id": "t134",
        "is_done": False
    }
    res=requests.put(url=url,json=data)

    #check right status code
    assert res.status_code==200

    #https://codebeautify.org/json-to-json-schema-generator
    schema={
        "$schema": "http://json-schema.org/draft-06/schema#",
        "$ref": "#/definitions/Welcome2",
        "definitions": {
            "Welcome2": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "task": {
                        "$ref": "#/definitions/Task"
                    }
                },
                "required": [
                    "task"
                ],
                "title": "Welcome2"
            },
            "Task": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "user_id": {
                        "type": "string",
                        "format": "integer"
                    },
                    "content": {
                        "type": "string"
                    },
                    "is_done": {
                        "type": "boolean"
                    },
                    "created_time": {
                        "type": "integer"
                    },
                    "task_id": {
                        "type": "string"
                    },
                    "ttl": {
                        "type": "integer"
                    }
                },
                "required": [
                    "content",
                    "created_time",
                    "is_done",
                    "task_id",
                    "ttl",
                    "user_id"
                ],
                "title": "Task"
            }
        }
    }   
    
    #validate coming response json is expected one
    validate(instance=res.json(),schema=schema)

