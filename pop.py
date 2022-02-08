import array as arr
a=arr.array('i',[1,2,3])
print("the new created array is :",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print("the pop element is :",end=" ")
print(a.pop(1))
print("the array elements after popping is :",end="")
for i in a:
    print(i,end=" ")
