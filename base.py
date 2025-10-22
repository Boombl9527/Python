"""

print(666)
print(13.14)
print("熟能生巧")


# 单行注释使用#

# 注意有个空格

#print(内容1,内容2,内容3，...,内容N)
money = 50
print("钱包还有：",money)

#买了一个冰淇淋
money = money - 10
print("买了冰淇淋花了10元，还剩",money,"元")

#每隔一小时输出钱包的余额
print("现在是下午1点，钱包余额剩余：",money,"元")
print("现在是下午2点，钱包余额剩余：",money,"元")
print("现在是下午3点，钱包余额剩余：",money,"元")
print("现在是下午4点，钱包余额剩余：",money,"元")
print("现在是下午5点，钱包余额剩余：",money,"元")

#小练习
money = 50
print("当前钱包余额：",money,"元")
print("购买了冰淇淋，花费：10元")
print("购买了可乐，花费：5元")
money = money - 10 - 5
print("最终，钱包剩余：",money, "元")

#type()
money = 50
money_type = type(money)
print(money_type)
print(type(money_type))
true_type = type(True)
print(true_type)
#在Python中变量是没有类型的，只是它存储的数据有类型。


num_str = str(11)
print(num_str)
print(type(num_str))
num_int = 11
print(num_int)
print(type(num_int))

num = float(20)
print(num)
print(type(num))


print("10 / 3 = ",10/3)

name =  "\"换行测试\""
print(name)
"""

"""
name = "王子龙"
address = "兰台府"
tel = "1711748105"
habit = "玩游戏"
print("我是" + name + "，我住在" + address)
print("我是" + name + "，我住在" + address + "，我的电话是：",tel , "，我的爱好是" + "habit")
print("我是" + name + "，我住在" + address + "，我的电话是："+ tel + "，我的爱好是" + "habit")
print("我是", name,  "，我住在",  address, "，我的电话是：",tel, "，我的爱好是" , "habit")


study_time = 5.135
print("我相信编程没有这么难，一切的事情都是熟能生巧，我已经学习了%.3f小时了" % study_time)
print(f"我相信编程没有这么难，一切的事情都是熟能生巧，我已经学习了{study_time}小时了")
"""









