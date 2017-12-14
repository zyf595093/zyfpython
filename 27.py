import math
def move(x,y,step,angle=0):
    nx = x + step*math.cos(angle)
    ny = y - step*math.sin(angle)
    return nx,ny

x,y =move(100,100,60,30)
print (x,y)

print ('一元二次方程解答')
print ('a*x**2+b*x+c=0')
a=float(input('请输入a='))
b=float(input('请输入b='))
c=float(input('请输入c='))
if (b**2-4*a*c)>=0:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print(x1,x2)
else:
    print ('该方程无实数解，有共轭负根')