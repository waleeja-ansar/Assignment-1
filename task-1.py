
list1 = input("Enter first list elements (space separated): ").split()
list2 = input("Enter second list elements (space separated): ").split()

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

list1.extend(list2)

list1.sort()

print("Merged and Sorted List:", list1)
