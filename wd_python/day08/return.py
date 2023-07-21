"""
return 返回值
Author:LXQing
Date:2023/6/28
"""
# 没有输入 直接返回值
def weather():
    temp=37.3
    wet=30
   # print('温度: ',temp,'°')
    return temp,wet
if __name__ == '__main__':
#  weather()
    a,b=weather()
    print('有两个返回值就要写两个参数',a,b)

