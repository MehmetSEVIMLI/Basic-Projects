list=[]

rang=int(input("text a range: "))

for i in range(rang):
    nums=int(input("tex a number:  "))
    list.append(nums)
    
list_add=sum(list)

mean=list_add/rang

print("mean: ",mean)