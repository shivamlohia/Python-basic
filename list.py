arr = [1,2,3,4,5,6,7,8,9,10]
el1 = arr[-1]   #gets last element, -2 gets last second and so on
el2 = arr[::-1] #gets list in reverse

print(arr, "last element", el1)
print("arr in reverse", el2)

arr.append(12)
print("After appending 12" ,arr)

arr.insert(10,11)
print("After inserting 11", arr)


arr2 = [13,15,14,15]
arr.extend(arr2)
print("arr after extension", arr)

index_of_15 = arr.index(15)
print("Index of 15", index_of_15)

count_of_15 = arr.count(15)
print("Count of 15", count_of_15)

popped = arr.pop(13)
print("arr after pop with index", arr, ". Popped element", popped)

popped = arr.pop()
print("arr after pop without index", arr, ". Popped element", popped)

print("Length of arr", len(arr), ". Sum =", sum(arr))

print("arr2 sorted:", sorted(arr2))

arr2.clear()
print("arr2 after clear", arr2)

arr2 = ["abc", "cad", "cda", "bca", "baa", "bac"]
print(arr2, "= arr2. Sorted arr2: ", sorted(arr2))
print(arr2)

arr.append(15)
cubed = [num ** 3 for num in arr if num % 5 == 0]
print("Cubed 5 multiples", cubed)