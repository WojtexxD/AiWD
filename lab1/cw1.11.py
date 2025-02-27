words=["apple", "banana", "apple", "orange", "banana", "apple"]
wynik = {x: words.count(x) for x in words}
print(wynik)