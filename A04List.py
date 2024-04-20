#List are mutable in nature 
'''List is mutable in nature can contain mutiple values '''

marks = [1,2,3,4,5]
print(marks)

marks2 = [7.6, 8.9, 9.0, 7.9]
print(marks2)

name = ["Anuj", "Anja", "Anjali", "Aman", "Navin"]
print(name)

list1 = [1, "anuj", 7.9, True]
print(list1)

listContact = [marks, marks2]
print(listContact)



list1.append("Anjali")  # append value at the end
print(list1)

list1.insert(1, 99) # insert value at index
print(list1)

list1.remove("anuj") # remove value
print(list1)

list1.pop() # pop out value from end
print(list1)

list1.pop(0) # pop out at any index +ve/-ve index
print(list1)

list1.extend(["Anuj", True, "Anuj", False, 12909, 1.2, 5/2, 9**2])  # extends the list 
print(list1)

print(list1.index("Anuj", 0, 6)) # returns 1st index of any value in range

marks2 = [23, 45, 67, 9.0, 45.76, 85.3, 1000, 4.5, 5, 6, 555, ]

print(min(marks2))
print(max(marks2))
print(sum(marks2))

marks2.sort()
print(marks2)