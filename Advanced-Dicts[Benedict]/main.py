from benedict import benedict

people:dict={
          "name":"utsav",
          "age":22
}

people_benedict=benedict(people)

# Can accessed with '.'
print(people_benedict.name," ",people_benedict.age)

people_benedict2=benedict()

# Can reconstruct with dict with '.'
people_benedict2.name="supu"
people_benedict2.age=21
print(people_benedict2)

special_dict=benedict(keyattr_dynamic=True)

special_dict.a.b.d=500
print(special_dict)

# Can form dicts from files also...
print(benedict.from_json('students.json'))
print(benedict.from_xml('students.xml'))

student={
      "root":[
                {"name":"utsav","age":22},
                {"name":"supu","age":21}
      ]
}

st=benedict(student)

with open('test.json','w+') as f:
          f.write(st.to_json())
