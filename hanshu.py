def hanshu(a):
    for i in range(len(a)):
        print (str(a[i-1]),end=',')
    print ('and',(a[-1]))
        
a=[1,2,3,4,5,6,7,8,9]
hanshu(a)

        