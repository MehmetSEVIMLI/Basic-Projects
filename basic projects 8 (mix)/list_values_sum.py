list=[int(i) for i in input("text a values: ").split(" ")]

add_values=0

for i in range(len(list)):
    add_values+=list[i]
print(add_values)