
Number_of_animals = {"dogs": 30, "cows": 40, "cats": 12, "sheep": 55}
print(type(Number_of_animals))
print(Number_of_animals.values())
print(Number_of_animals.keys())

for i in Number_of_animals:
    print(i)


z = "geeks"
for letters in z:
    print(letters)

x = [z + " for geeks"]
print(x)
for i in x:
    print(i)

sum = 0
numbers = [1, 2, 3, 56, 45, 89, 90, 12, 23, 24]
for y in numbers:
    sum = sum + y
    print("The total sum is ", sum)

for c in range(1, 100, 2):
    print(c)
for t in range(2, 100, 2):
    print(t)
    


for i in range(50, 100):
    if i % 2 == 0:
        print(i, " is divisible by 2")
    else:
        print(i, " is not divisible by 2 ")






