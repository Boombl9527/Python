guess_num = 10
if int(input("请输入第一次猜想的数字：")) == guess_num:
    print("恭喜你猜对啦")
elif int(input("不对，再猜最后一次：")) == guess_num:
    print("恭喜你猜对啦")
elif int(input("不对，再猜一次")) == guess_num:
    print("恭喜你猜对啦")
else:
    print(f"Sorry,全部猜错啦，我想的是：{guess_num}")
