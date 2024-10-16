list1 = [-10, -8, 2, 4, 6]
list2 = [4, 16, 36, 64, 100]

# Concatenate two lists
list1 = list1 + list2

# sorting using in-build function
list1.sort()
print(list1)

# Bubble sorting
for i in range(len(list1)):
    swapped = False
    for j in range(0, len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list[j+1] = list1[j+1], list1[j]
            swapped = True
    if not swapped:
        break

print("Sorted Array list ", list1)



