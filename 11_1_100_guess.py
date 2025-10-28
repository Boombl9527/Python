import random
num = random.randint(1,100)
print(f"随机数是{num}和{num - 1}")
print(type(num))

guess_num = 0
guess_times = 0
while guess_num != num:
    guess_num = int(input(f"请进行第{guess_times}次猜测：\n"))
    guess_times += 1
    if guess_num == num:
        print(f"恭喜您用了{guess_times}次就猜中啦")
    else:
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")

print(num)

