students = {
    "Alice": {"math": 4, "english": 5, "history": 3},
    "Bob": {"math":3, "english": 3, "history": 4}
}

# students["Karol"] = {"math": 2, "english": 3, "history": 4}
students.update({"Karol": {"math": 2, "english": 3, "history": 4}})
print(students)

averages={name:sum(grades.values())/len(grades) for name, grades in students.items()}
print(averages)

# wynik=0
# temp=0
# for key, value in students.items():
#     for x, y in value.items():
#         wynik+=y
#         temp+=1
#     print(wynik/temp)
#     temp=0
#     wynik=0