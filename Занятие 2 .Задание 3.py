def Время(min):
    hour = min // 60
    min %= 60
    return "%02d:%02d" % (hour, min)
n=int(input())
print(Время(n))