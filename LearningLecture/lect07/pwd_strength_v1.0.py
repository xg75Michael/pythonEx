"""
    作者： Michael Gao
    功能： 判断密码强度
    版本： 1.0
    日期： 25／11／2018
"""


def check_number_exist(password_str):
    """
        判断字符串中是否含有数字
    """
    for c in password_str:
        if c.isnumeric():
            return True
    return False


def check_letter_exist(password_str):
    """
        判断字符串中是否含有字母
    """
    for c in password_str:
        if c.isalpha():
            return True
    return False


def main():
    """
        主函数
    """
    password = input('请输入密码： ')

    # 密码强度变量
    strength_level = 0

    # 规则一： 密码长度大于等于8
    if len(password) >= 8:
        strength_level += 1
    else:
        print('密码要求至少8位！')

    # 规则二： 密码包含数字
    if check_number_exist(password):
        strength_level += 1
    else:
        print('密码要求包含数字！')

    # 规则三： 密码包含字母
    if check_letter_exist(password):
        strength_level += 1
    else:
        print('密码要求包含字母！')

    if strength_level == 3:
        print('恭喜恭喜，密码强度合格！')
    if strength_level != 3:
        print('恭喜恭喜，密码强度不不不不合格！')


if __name__ == '__main__':
    main()



