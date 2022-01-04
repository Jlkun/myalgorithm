
# print("周杰伦")

#format函数的用法


# var1="{1} {0}".format("hello","python")
# var1="{} {}".format("hello","python")
# print(var1)  #python hello

import random

# print(oct(1234))
# print(hex(1234))
# print(oct(1234).replace('0o', '0') + " " + hex(1234).upper())

#选择排序 找一个最小值，记录进行排序
def choicearr(charr):
    arrlength= len(charr)
    # print(arrlength)
    for i in range(0,arrlength):
        minmun=i  #定义最小的数的位置，从0开始
        for j in range(i+1,arrlength): #内循环里面进行第一轮比较，选出最小的数的位置。
            if charr[j]<charr[minmun]:
                minmun=j
        charr[minmun],charr[i]= charr[i],charr[minmun]#交换放在第一个位置

    # print(arr2)

#冒泡排序 相隔两位数进行比较
def maopaoarr(maoarr):
    maoarrlength=len(maoarr)
    for i in range(1,maoarrlength): #在length-1个位置循环
        for j in range(maoarrlength - i): #在0-length-i的位置循环
            if(maoarr[j]>maoarr[j+1]):
                temp = maoarr[j]
                maoarr[j] = maoarr[j+1]
                maoarr[j+1] = temp
    print(maoarr)




sortarrtest=[2,1,3,5,4]
# print (arrtest)

# choicearr(sortarrtest)
# maopaoarr(sortarrtest)

#python中的与 (and)，或(or)，异或（^ 不同为1，相同为0，0和任何数亦或=任何数）
#用异或实现交换
a=17;b=13
a=a^b
b=a^b
a=a^b

#数组中有一种数出现了奇数次，其他所有的数出现偶数刺。找出奇数次数组
yharrtest1=[2,2,3,3,4]
eor=0
for i in yharrtest1:
    eor^=i
# print (eor)

#数组中有2种数出现了奇数次，其他所有的数出现偶数刺。找出奇数次数组
yharrtest2=[2,2,6,7]
eor=0;onlyeor=0;
for i in yharrtest2:
    # ax=i^eor
    eor^=i

rightOne =eor & (~eor+1)
onlyOne =0
for i in yharrtest2:
    if (i&rightOne==0):
        onlyOne^=i

# print(onlyOne)
# print(onlyOne^eor)


#按照算法可能遇到的最差情况的时间复杂度
#插入排序 挨个排好序，把剩余的数往里插
def insertsortarr(insarr):
    insarrlen=len(insarr)
    for i in range(1,insarrlen): #默认第一个数是排好序的，所以在1-len上循环
        for j in range(i,0,-1): #倒着进行循环，每次最坏需要比较i次
            if(insarr[j-1]>insarr[j]):
                insarr[j],insarr[j-1]=insarr[j-1],insarr[j]
    # print(insarr)
sortarrtest1=[2,1,3,5,4]
# insertsortarr(sortarrtest1)

#二分法

def orderarrtt(orderarr,num):
    low =0
    high=len(orderarr)-1
    min=0
    while(low<=high):
        orderlen = len(orderarr)//2
        if(orderarr[orderlen]>num):
            orderarr=orderarr[0,orderlen//2]
        elif(orderarr[orderlen//2]<num):
            orderarr = orderarr[orderlen // 2+1, orderlen]
        elif (orderarr[orderlen // 2] ==num):
            pass

orderarrtest2=[1, 2, 3, 4, 5]
# orderarrtt(orderarrtest2)

#在一个有序数组中找到>=某个数最左侧的位置(依然可以二分)1222333444。找到第一个3的位置，也就是最左侧的位置

#局部最小问题 一个无序数组中，所有相邻的数一定不相等，找到任意一个局部最小的一个数。局部最小数定义，如果一个数比左边和右边的数都小，则为局部最小数

#对数器的概念

#递归 求数组中的最大值 
#递归就好像是一颗二叉树，利用栈做了后序遍历，从树的最后分支一直往上汇总。
#递归的时间复杂度是o(n)
def diguiarrmax(L,R,diarr):
    if (L==R):
        return diarr[L]
    # min1=L+(R-L)//2  #这么写是为了防止数组溢出
    min=L+((R-L)>>1) #更装逼的写法 右移n位就相当于除以2的n次方
    leftmax=diguiarrmax(L,min,diarr)
    rightmax=diguiarrmax(min+1,R,diarr)
    return max(rightmax,leftmax)

diguiarrtest=[1, 2, 3, 4, 5,6]
# print(diguiarrmax(0,len(diguiarrtest)-1,diguiarrtest))
"""
递归中的master公式 T(n)=a*T(N/b)+o(N^d)
a代表递归调用次数，二分法中递归调用次数为2次
b代表子问题的规模，二分法中将数组一分为二，b为2
后年的oN代表除了递归之外的时间复杂度。
并不是所有的递归都可以套用master公式，当子问题的规模不一样的时候，不符合。例如前1/3区域调递归，后面2/3区域调递归 

①当d<logb a时，时间复杂度为O(n^(logb a))
②当d=logb a时，时间复杂度为O((n^d)*logn)
③当d>logb a时，时间复杂度为O(n^d) 
"""

'''如果这世界上真有奇迹，那只是努力的另一个名字'''

#归并排序 时间复杂度n*log(n) 空间复杂度o（n）
'''选择，冒泡，插入浪费了大量的比较行为，'''

#一个数组左侧有序，右侧也有序。排序
"""
"""
def megesortarr(merarr):
    if len(merarr) <= 1:
        return merarr
    mid = len(merarr)//2
    leftarr=megesortarr(merarr[:mid])
    rightarr=megesortarr(merarr[mid:])
    return merge(leftarr,rightarr) #递归让左右都先有序，

def merge(leftarr,rightarr): #merge函数让有序的左右排序进行排序达到整体有序
    helplist=[]
    j=h=0
    while(j<len(leftarr) and  h<len(rightarr)): #当左右都不溢出的情况，把小的放进help数组
        if(leftarr[j]<rightarr[h]):
            helplist.append(leftarr[j])
            j+=1;
        else:
            helplist.append(rightarr[h])
            h+=1;
    while(j<len(leftarr)): #当左边还有值的时候，说明右边已经排完了，这个时候把左边剩下的数直接拼接进入help中
        # print(leftarr[j:])
        helplist=helplist+leftarr[j:]
        break
    while (h<=len(rightarr)):#右边同理左边
        # print(rightarr[h:])
        helplist=helplist+rightarr[h:]
        break
    return helplist
sortarr=[4,5,3,8,1,6,9]
# print((megesortarr(sortarr)))


#归并排序的扩展 小和问题
"""
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数的小和。求一个数组的小和。
例子：[1,3,4,2,5]。
1左边比1小的数：没有；
3左边比3小的数：1；
4左边比4小的数：1,3；
2左边比2小的数：1；
5左边比5小的数：1,3,4,2；
所以小和为1+1+3+1+1+3+4+2=16
"""
#小和问题暴力解法
def xiaohearr(xharr):
    if(len(xharr)==1):
        return 0
    arrmun=0
    for i in range(1,len(xharr)-1):
        for j in range(i,0,-1):
            if xharr[j]<xharr[i]:
                arrmun=arrmun+xharr[j]
    return arrmun

xiaohearrtest=[1,3,4,2,5]
# print(xiaohearr)

#归并排序的扩展 逆序对问题
"""
在一个数组中，左边的数比右边的数大，则这两个数构成一个逆序对，打印所有的逆序对
"""
#逆序对问题暴力解法
def nixuduiarr(nxdarr):
    for i in range(len(nxdarr)-1):
        for j in range(i+1,len(nxdarr)):
            if(nxdarr[j]<nxdarr[i]):
                print(nxdarr[i],nxdarr[j])

nxdarrtest=[3,2,4,5,0]
(nixuduiarr(nxdarrtest))


