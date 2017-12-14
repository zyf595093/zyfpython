a = int(input('请输入小明去年的成绩='))
b = int(input('请输入小明今年的成绩='))
if b-a>0:
    percent=100*(b-a)/a
    print('小明成绩比去年提高了%.1f %%' %percent)
elif b-a<0:
    percent=100*(a-b)/a
    print('小明成绩比去年下降了%.1f %%' %percent)
else:
    print('小明成绩没有变化')
    
    