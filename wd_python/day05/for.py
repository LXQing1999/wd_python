"""
for 
Author:25423
Date:2023/6/25
"""
def circulation():
    a=[1,2,3,4]
    for i in a:
        print(i,end=' ')


def scope():
    for i in range(10):
        print(i,end=' ')

if __name__ == '__main__':
    circulation()
    print('\n')
    scope()