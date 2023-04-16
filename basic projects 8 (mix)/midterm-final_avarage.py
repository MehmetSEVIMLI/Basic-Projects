midterm=int(input("text a midterm point: "))
final=int(input("text a final point: "))

avarage_midterm=midterm*0.4
avarage_final=final*0.6

avarage_total=avarage_midterm+avarage_final

if avarage_total>=50:
    print("PASS the exam.\ntotal avarage: ",avarage_total)
else:
    print("FAILED the exam.\ntotal avarage: ",avarage_total)