"""
capture_error 捕捉异常

Author:LXQing
Date:2023/7/1
"""
def exception_sperate():
    # try:
    #     num = int(input('请输入一个整数:'))
    #     print(num)
    # except:
    #     # 出现异常的处理
    #     print('请输入整数:')
    # print('保证代码的健壮性')
    try:
        num = int(input('请输入整数:'))
        result = 8 / num
        print(result)
    except ValueError:
        print('请输入正确的整数')
    except ZeroDivisionError:
        print('除0错误')
    except Exception as result:
        print('未知错误%s'%result)
    else:
        print('正常执行')
    finally:
        print('执行完成,无论是否有异常,都会执行')

if __name__ == '__main__':
    exception_sperate()