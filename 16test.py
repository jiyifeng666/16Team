# -*- coding:utf-8 -*-

biaoti = input("Please enter a title:")
num = input("Please enter how many people to vote:")
dic = {
    "yes":0,
    "no":0,
}
for i in range(int(num)):
    piao = input("Please vote(1.yes  2.no)")
    if piao == "1":
        dic["yes"] += 1
    elif piao == "2":
        dic["no"] += 1
    print(f"The current number:yes----{dic['yes']}ticket,no----{dic['no']}ticket")
