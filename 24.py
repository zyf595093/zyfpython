# _*_ coding: utf-8 _*_

xiaoMingHeight = float(input('请输入小明身高(单位米)'))
xiaomingWeight = float(input('请输入小明体重(单位千克)'))
xiaomingBMI = xiaomingWeight/xiaoMingHeight**2
print('BMI=%.1f' %xiaomingBMI)
if xiaomingBMI<18.5:
    print('小明体重过轻')
elif xiaomingBMI<25:
    print('小明体重正常')
elif xiaomingBMI<28:
    print('小明体重过重')
elif xiaomingBMI<32:
    print('小明体重肥胖')
else:
    print ('小明体重严重肥胖')

