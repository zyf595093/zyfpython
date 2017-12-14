def hanNuoTa(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        hanNuoTa(n-1,a,c,b)
        print(a,'-->',c)
        hanNuoTa(n-1,b,a,c)
        
        
x=int(input('请输入汉诺塔的个数='))
hanNuoTa(x,'A','B','C')
