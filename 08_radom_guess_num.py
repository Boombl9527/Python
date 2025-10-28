"""
import random
num =random.randint(1,10)

guess_num = int(input("请输入第一次猜测："))
if guess_num == num:
    print("恭喜您猜中了！")
else:
    if guess_num < num:
        print("猜小了")
        guess_num = int(input("请输入第二次猜测："))
        if guess_num == num:
            print("恭喜您猜中了！")
        else:
            if guess_num < num:
                print("猜小了")
                guess_num = int(input("请输入第三次猜测："))
                if guess_num == num:
                    print("恭喜您猜中了！")
                else:
                    if guess_num < num:
                        print("猜小了，机会耗尽。")
                    else:
                        print("猜大了，机会耗尽。")

            else:
                print("猜大了")
                guess_num = int(input("请输入第三次猜测："))
                if guess_num == num:
                    print("恭喜您猜中了！")
                else:
                    if guess_num < num:
                        print("猜小了，机会耗尽。")
                    else:
                        print("猜大了，机会耗尽。")

    else:
        print("猜大了")
        guess_num = int(input("请输入第二次猜测："))
        if guess_num == num:
            print("恭喜您猜中了！")
        else:
            if guess_num < num:
                print("猜小了")
                guess_num = int(input("请输入第三次猜测："))
                if guess_num == num:
                    print("恭喜您猜中了！")
                else:
                    if guess_num < num:
                        print("猜小了，机会耗尽。")
                    else:
                        print("猜大了，机会耗尽。")

            else:
                print("猜大了")
                guess_num = int(input("请输入第三次猜测："))
                if guess_num == num:
                    print("恭喜您猜中了！")
                else:
                    if guess_num < num:
                        print("猜小了，机会耗尽。")
                    else:
                        print("猜大了，机会耗尽。")
"""

import random
num =random.randint(1,10)

guess_num = int(input("请输入您的猜测第一次猜测："))

if guess_num == num:
    print("恭喜您猜对啦！")
else:
    if guess_num > num:
        print("猜大了。")
    else:
        print("猜小了。")

    guess_num = int(input("请输入您的猜测第二次猜测："))

    if guess_num == num:
        print("恭喜您猜对啦！")
    else:
        if guess_num > num:
            print("猜大了。")
        else:
            print("猜小了。")

        guess_num = int(input("请输入您的猜测第三次猜测："))
        if guess_num == num:
            print("恭喜您猜对啦！")
        else:
            if guess_num > num:
                print("猜大了，机会耗尽。")
            else:
                print("猜小了，机会耗尽。")

# 打印一个num，测试功能。
print(num)




