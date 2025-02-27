person = {"name": "John", "age": 30, "city": "New York"}
for x in person:
    print(x,person[x])

for key, value in person.items():
    print(f"{key}:{value}")