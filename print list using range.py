import array as arr
l=[2,5,6,9,11,5,7,8,3]
a=arr.array('i',l)
print("the new created array is :",end=" ")
for i in a[0:5]:
    print(i,end=" ")
Sliced_array=a[3:9]
print(Sliced_array)