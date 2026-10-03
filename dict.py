dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}

merged = {**dict1, **dict2}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged dictionary:", merged)

sorted_dict = dict(sorted(merged.items()))
print("Sorted dictionary:", sorted_dict)

text = input("Enter a word: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:", frequency)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Common elements:", set1 & set2)
print("Unique elements in set1:", set1 - set2)
print("Unique elements in set2:", set2 - set1)