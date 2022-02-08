import array as arr
a=arr.array("d",[2.5,3.2,3.3])
print("array before insertion :",end="")
for i in range (0,3):
    print(a[i],end=" ")
a.append(5.5)
print("array after insertion :",end="")
for i in a:
    print(i,end=" ")
