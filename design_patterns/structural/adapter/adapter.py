from typing import Protocol

import xml.dom.minidom

import os

os.chdir(r'D:\\advance-python\\design_patterns\\structural\\adapter')

"""
we have a xml to txt converter here...
"""

class ITool(Protocol):

    def write(self,text):...

    def convert_txt(self):...

class ConverterXmlToTxt(ITool):
    """
    only able to parse xml's.
    """
    def __init__(self,file:str,key:str) -> None:
        self.filename=file.split('.xml')[0]
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement
        self.group = collection.getElementsByTagName(key)
    
    def write(self,text:str):
        with open(self.filename+'.txt','a') as fs:
            fs.write(text+'\n')
        fs.close()
    
    def convert_txt(self):
        for item in self.group:
            self.write('*******Student*******')
            id=item.getElementsByTagName('id')[0].childNodes[0].nodeValue
            name=item.getElementsByTagName('name')[0].childNodes[0].nodeValue
            age=item.getElementsByTagName('age')[0].childNodes[0].nodeValue
            self.write(f"id : {id}")
            self.write(f"name : {name}")
            self.write(f"age : {age}")



#c=ConverterXmlToTxt(file='students.xml',key='student')
#c.convert_txt()
    
"""
now for some reason I need a json to txt converter
"""
import json

class ConverterJsonTxt(ITool):
    """
        only able to parse json's.
    """

    def __init__(self,file:str,key:str) -> None:
        self.filename=file.split('.json')[0]
        self.key=key
        with open("students.json", "r") as read_file:
            self.data = json.load(read_file)
        read_file.close()

    def write(self, text):
        with open(self.filename+'.txt','a') as fs:
            fs.write(text+'\n')
        fs.close()
    
    def convert_txt(self):
        for item in self.data[self.key]:
            self.write('*******Student*******')
            id=item['id']
            name=item['name']
            age=item['age']
            self.write(f"id : {id}")
            self.write(f"name : {name}")
            self.write(f"age : {age}")

#c=ConverterJsonTxt(file='students.json',key='student')
#c.convert_txt()

"""
now the situation is that I don't know when the incoming file is .json and when it is .xml. 
SO , I need a adapter here for both type compatibility.
"""

class ConverterTxt:
    """
    its a adapter which can dynamically convert.
    """

    def __init__(self,file:str,key:str) -> None:
        self.type=file.split(".")[1].upper()
        self.file=file
        self.key=key

    def convert_txt(self):
        if self.type=='JSON':
            return ConverterJsonTxt(file=self.file,key=self.key).convert_txt()
        elif self.type=='XML':
            return ConverterXmlToTxt(file=self.file,key=self.key).convert_txt()

c=ConverterTxt(file='students.xml',key='student')
c.convert_txt()
