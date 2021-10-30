m=int(input('enter the month :'))
if m==1 or 3 or 5 or 7 or 8 or 10 or 12:
    print('month',m,' have 31 days')
elif m== 2 :
    print('month',m,'have 28 days')
else :
    print('month',m,'have 30 days')
