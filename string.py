text = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")

replaced = text.replace(old, new)
print("After replacement:", replaced)

reverse = text[::-1]
print("Reversed string:", reverse)

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

ch = input("Enter a character to count: ")
print("Character frequency:", text.count(ch))

word = input("Enter a word to count: ")
words = text.split()
print("Word frequency:", words.count(word))