number=[int(i) for i in input("text number: ")]

multi=1

for i in range(len(number)):
    multi*=number[i]
print(multi)