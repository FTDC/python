def printme(str):
    print("打印传入的字符串")
    print(str)
    return


printme("nihao")


def changeme(mylist):
    "修改串串的参数列表"
    mylist.append([1, 2, 3, 4, 5])
    print("函数内的取值:", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值:", mylist);

# 匿名函数
sum = lambda arg1, arg2, arg3: arg1 + arg2 * arg3
print(sum(1, 2, 3));


def sum(arg1, arg2):
    return arg1 + arg2;


print(sum(12, 2));
