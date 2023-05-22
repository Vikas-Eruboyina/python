def pwd(str1):
    if len(str1) < 8:
        print('Entered pwd is too short')
    u = 0
    l = 0
    s = 0
    d = 0
    sp=['!','@','#','$','%','^','&','*']
    for i in str1:
        if i.isupper():
            u +=1
        elif i.islower():
            l +=1
        elif i in sp :
            s +=1
        elif i.isdigit():
            d +=1
    if u == 0:
        print('Enter atleast one Upper case letter')
    if l == 0:
        print('Enter atleast one lower case letter')
    if s == 0:
        print('Enter atleast one  special character')
    if d ==0:
        print('Enter atleast one number')
        
x= input('Enter your Password ')
pwd(x)
       
