import array as arr
a=arr.array('i',[1,2,3])
print("the new created array is :",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
a.insert(1,4)
print("array after insertion ",end=" ")
for i in (a):
    print(i,end=" ")
print()
