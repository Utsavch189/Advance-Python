from dataclasses import dataclass,field,asdict
import json
from typing import List

@dataclass
class Result:
    cls:str=field(default_factory=str)
    marks:int=field(default_factory=int)

@dataclass
class Student:
    name:str=field(default_factory=str)
    results:List[Result]=field(default_factory=list)

    def __post_init__(self):
        self.results=[Result(**i) for i in self.results]
    
    def toJson(self):
        # deserialize
        return json.dumps(asdict(self),indent=4)

"""
Serialization is the process of converting an object into a format 
that can be easily stored, transmitted, or reconstructed at a later time. 
This is particularly useful when you want to save the state of an object to 
disk or send it over a network.
"""

# EX-> 
with open('test.json','r') as f:
    jsonn=json.loads(f.read())

student=Student(**jsonn)
print(student) # --> Student(name='Utsav Chatterjee', results=[Result(cls=1, marks=60), Result(cls=2, marks=88), Result(cls=3, marks=74)])

# here incoming json converts into python object. It's Serialization.

# .......................................................................................................................................................................

"""
Deserialization, on the other hand, 
is the process of reconstructing an object from its serialized form.
"""

#EX->
student_json=student.toJson()
print(student_json) 
"""
{
    "name": "Utsav Chatterjee",
    "results": [
        {
            "cls": 1,
            "marks": 60
        },
        {
            "cls": 2,
            "marks": 88
        },
        {
            "cls": 3,
            "marks": 74
        }
    ]
}
"""
with open('output.json','w') as f:
    f.write(student_json)