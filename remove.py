import array as arr
a=arr.array('i',[1,2,3,1,4,1])
print("the new created array is :",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print("the removed element is :",end=" ")
a.remove(1)
a.remove(1)
a.remove(1)
print("the elements after removing :")
for i in a:
    print(i,end=" ")
