"""
Enums are generally used for collection of predefine data or constants...
"""

from enum import Enum

class Weeks(Enum):
    sunday=1
    monday=2
    tuesday=3
    wednesday=4
    thursday=5
    friday=6
    saturday=7
    extra=['hi','hello']
    
print(Weeks.sunday.value)
print(Weeks['friday'].value)
print(Weeks(5).name)
print(Weeks.extra.value)