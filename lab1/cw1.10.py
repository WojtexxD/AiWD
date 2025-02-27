student = {"name": "Anna", "age": 22, "major": "Computer Science"}
student["grades"] =[4.5,5.0,3.5]
# student["age"] = 23
student.update({"age": 23})
# del student["major"]
student.pop("major")
print(student)