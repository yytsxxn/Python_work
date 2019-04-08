#1_冒泡排序
lis = [56,12,1,8,354,19,10,100,34,56,7,23,456,234,-58]
def sortport(lis):
    for i in range(len(lis) - 1):
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis
#print( sortport(lis) )

#2_x的n次方
#pow(2,10)
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s *= x
    return s
#print( power(2,10) )


#3_不确定个数个参数 求平方和
#*numbers 收集参数

def cal( *numbers ):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
#print( cal(1,2,3,4,5,6,7) )

#4_求 n！
def fac():
    num = int( input("请输入一个数字: ") )
    factorial = 1
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1,num + 1):
            factorial *= i
        print("%d的阶乘为%d" % (num,factorial))
#fac()

#4_1递归方法求n!
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n - 1)
#print( factorial(5) )

#5_以列表的形式，输出当前目录下所有的文件名
import os
#print( [d for d in os.listdir(".")] )

#6_输出指定路径下的所有文件名  【C:// || C:\ 】
def print_dir():
    filepath = input("请输入一个路径：")
    if filepath == " ":
        print("请输入正确的路径！")
    else:
        for i in os.listdir(filepath):
            print(os.path.join(filepath,i))
#print_dir()

#7_把列表中的字符串中的大写字母转换为小写
li = ["HELLO","WORLD","I LIKE","APPLE"]
#print( [s.lower() for s in li] )

#8_颠倒键值
dict1 = {"A":"a" , "B":"b" , "C":"c"}


#9_ 9*9 乘法表
def che():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d * %d = %d\t" % (i,j,i*j),end="")
#che()

#10_改变列表中的某个特定值 3 —> 3a
def change(num):
    for i in range(num.count(3)):
        ele_index = num.index(3)
        num[ele_index] = "3a"
    return num
#print( change([1,2,3,4,5,6,1,2,3,3,35,6]) )

#11_列表合并去重  集合
list1=[2,3,8,4,9,5,6]
list2=[5,6,10,17,11,2]
list3= list1+list2
#print(list3)
#print(set(list3))
#print(list(set(list3)))

#12_随机生成验证码 两种方式
#第一种
import random
list1=[]
for i in range(65,91):
    list1.append(chr(i))
for j in range(97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))
ma = random.sample(list1,6) #从list1中随机取出6位
ma="".join(ma) #转化为字符串
#print(ma)
#第二种
import random,string
str1="0123456789"
str2=string.ascii_letters #将所有字母的ASCII码以字符串形式赋给str2
str3=str1+str2
ma = random.sample(str3,6)
ma = "".join(ma)
#print(ma)

#13_计算平方根
#num=float(input("请输入一个数字："))
#print(num**0.5)

#14_判断奇偶
while True: #true死循环
    try:
        num=int(input("请输入一个整数："))
    except ValueError:
        print("你输入的不是整数！")
    if(num%2 == 0):
        print("偶数")
    else:
        print("奇数")
    break  #跳出while循环

#15_判断闰年


#16_获取最大值
n = int( input("请输入需要比对大小的数字的个数:") )
print("请输入需要比对的数字")
num=[]
for i in range(1,n+1):
    temp = int( input("输入第%d个数字："% i) )
    num.append(temp)
print("您输入的数字为：",num)
print("最大值为：",max(num))

#17_斐波那契数列

#18_十进制数转换为二、八、十六进制

#19_简单计算器

#20_生成日历
import calendar
year=int( input("输入年份：") )
month=int( input("输入月份：") )
print(calendar.month(year,month))


