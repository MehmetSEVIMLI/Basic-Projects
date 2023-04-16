s=0
sub=0
indx=1
while s<2:
    sayi=int(input(f'{indx}. sayıyı giriniz: '))
    sub+=sayi
    s+=1
    indx+=1
print("sayılar toplamı: ",sub)