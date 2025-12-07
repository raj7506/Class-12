import array as arr
a = arr.array('i',[1, 2, 3])
print("\nThe new created array is: ", end=" ")
for i in range(0,3):
    print(a[i], end=" ")
print()
b = arr.array('d',[2.5, 3.2, 3.3])
print("\nThe new created array is: ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
a.insert(1, 4)
print("\nArray after intersection : ", end=" ")

array_num = arr.array('i', [1, 2, 3, 4, 3, 3])
print("Original array: "str(array_num))
print("Number of occurances of the number 3 in the said array: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))