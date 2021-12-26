
#working on dict using for loops
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
#finding the sum of numbers in a given list
sum = 0
numbers = [1, 2, 3, 56, 45, 89, 90, 12, 23, 24]
for y in numbers:
    sum = sum + y
    print("The total sum is ", sum)
    
#prints odd numbers between 1 and 100
for c in range(1, 100, 2):
    print(c)
    
 #prints out even numbers between 2 and 100   
for t in range(2, 100, 2):
    print(t)
    

#checking out the divisibility test of 2 between 50 and 100
for i in range(50, 100):
    if i % 2 == 0:
        print(i, " is divisible by 2")
    else:
        print(i, " is not divisible by 2 ")






