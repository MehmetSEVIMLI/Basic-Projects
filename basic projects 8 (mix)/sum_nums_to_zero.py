add=0
counter=0

while True:
    nums=int(input("text numbers: "))
    if nums==0:
        break
    else:
        add+=nums
        counter+=1
mean=add/counter
print("total: ",add)
print("total number count: ",counter)
print("mean: ",mean)