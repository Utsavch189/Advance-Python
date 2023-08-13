"""
Decorator Method is a Structural Design Pattern which allows you to dynamically attach new behaviors to 
objects without changing their implementation by placing these 
objects inside the wrapper objects that contains the behaviors. 
It is much easier to implement Decorator Method in Python because of its built-in feature. 
It is not equivalent to the Inheritance because the new feature is added only to that particular object, 
not to the entire subclass.
"""

class Write:
    def __init__(self,text:str) -> None:
        self._text:str=text
    
    def render(self)->None:
        return self._text

class Bold:

    def __init__(self,wrapper:object) -> None:
        self._wrapper:object=wrapper
    
    def render(self)->None:
        return '\033[1m'+self._wrapper.render()

if __name__=="__main__":
    text=Write("Utsav")
    bold_text=Bold(text).render()
    print(bold_text)

"""
Now suppose if I want to extend Italic Class....
"""

class Italic:
    def __init__(self,wrapper:object) -> None:
        self._wrapper:object=wrapper
    
    def render(self):
        return "\x1B[3m" + self._wrapper.render() + "\x1B[0m"

if __name__=="__main__":
    text=Write("Utsav")
    bold_text=Bold(text)
    bold_italic_text=Italic(bold_text)
    print(bold_italic_text.render())

"""
Now suppose if I want to extend Underline Class....
"""

class Underline:
    def __init__(self,wrapper:object) -> None:
        self._wrapper:object=wrapper
    
    def render(self):
        return f"\033[4m{self._wrapper.render()}\033[0m"

if __name__=="__main__":
    text=Write("Utsav")
    bold_text=Bold(text)
    bold_italic_text=Italic(bold_text)
    bold_italic_underline_text=Underline(bold_italic_text)
    print(bold_italic_underline_text.render())