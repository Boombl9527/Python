"""
print("欢迎来到黑马动物园")
height = int(input("请输入你的身高：\n"))

if height > 120:
    print("您的身高超出120cm，游玩需要补票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")

print("祝您游玩愉快。")


height = int(input("请输入你的身高：\n"))
vip_level = int(input("请输入您的vip等级（输入数字1-5）\n"))

if height < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif vip_level >=3:
    print("您的vip等级达到3级，可以免费游玩。")
else:
    print("不满足免费条件，需要买票。")

day = int(input("从日历接收日期：\n"))

if day ==1:
  print("今天是1号，全场免费。")
else:
    height = int(input("请输入你的身高：\n"))
    if height < 120:
        print("您的身高未超出120cm，可以免费游玩。")
    else:
        vip_level = int(input("请输入您的vip等级（输入数字1-5）\n"))
        if vip_level >= 3:
            print("您的vip等级达到3级，可以免费游玩。")
        else:
            print("不满足免费条件，需要买票。")

print("祝您游玩愉快！")
#print(height)同理
#print(vip_level)如果在height < 120的情况下会报错，原因是没有得到定义。


day = int(input("从日历接收日期：\n"))
height = int(input("请输入你的身高：\n"))
vip_level = int(input("请输入您的vip等级（输入数字1-5）\n"))
if day ==1:
  print("今天是1号，全场免费。")
elif height < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif vip_level >= 3:
     print("您的vip等级达到3级，可以免费游玩。")


print("祝您游玩愉快！")
"""

if int(input("从日历接收日期：\n")) ==1:
    print("今天是1号，全场免费。")
elif int(input("请输入你的身高：\n")) < 120:
    print("您的身高未超出120cm，可以免费游玩。")
elif int(input("请输入您的vip等级（输入数字1-5）\n")) >=3:
    print("您的vip等级达到3级，可以免费游玩。")
else:
    print("不满足免费条件，需要买票。")

print("祝您游玩愉快！")

