numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

x = int(input("Enter a number to search: "))

if x in numbers:
    print("Number found")
else:
    print("Number not found")

numbers[0] = 100
print("After update:", numbers)

even = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even)

numbers.append(60)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

numbers.sort()
print("Sorted list:", numbers)