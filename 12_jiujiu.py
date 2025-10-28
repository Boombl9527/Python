"""
print("Hello", end = '')
print("World", end = '')

print(len("DeltaForce\ttreasure"))
print(len("greed\t\tjudge"))

print("DeltaForce\ttreasure")
print("greed\t\tjudge")
"""

i = 1
j = 1
while j <= 9:
    while i <= j:
        print(f"{i}*{j}={i*j}\t", end ='')
        if i == j:
            print("隔断")
        i += 1
    i = 1
    j += 1

print("")

i = 1
j = 1
while i <=9:
    while j <= i:
        print(f"{i}*{j}={i*j}\t", end ='')
        if j == i:
            print("隔断")
        j += 1
    j = 1
    i += 1


