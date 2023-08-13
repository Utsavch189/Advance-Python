"""
Class should depend on interface rather than cocrete class
"""

"""
Suppose we have Bluetooth mouse and Wired mouse and same as Bluetooth keyboard and Wired keyboard
"""

class BluetoothMouse:
    ...
class WiredMouse:
    ...

class BluetoothKeyboard:
    ...
class WiredKeyboard:
    ...

class Macbook:
    def __init__(self) -> None:
        self._keyboard:WiredKeyboard=WiredKeyboard()
        self._mouse:WiredMouse=WiredMouse()

"""
This is wrong, if in future we want extend bluetooth system,
we can't because we hard coded here...
"""
#Sol-->

from typing import Protocol

class Mouse(Protocol):
    
    def wired(self):...

    def bluetooth(self):...

class Keyboard(Protocol):
    
    def wired(self):...

    def bluetooth(self):...

class Macbook:
    def __init__(self,mouse:Mouse,keyboard:Keyboard) -> None:
        self._keyboard:Keyboard=keyboard
        self._mouse:Mouse=mouse