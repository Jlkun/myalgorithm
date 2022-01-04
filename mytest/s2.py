

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
#
# print(onlyOne)
# print(onlyOne^eor)
#
#
# print((eor^2^2^6)^7)
#
# print(0^4^4^5)


# for i in range (5,0,-1):
#     print(i)


# print(10//2)
# print(1//2)
# print(3//2)
# print(max(11,1))


arr1=[1,2]
# print(type(arr1))


xiaohearrtest=[1,3,4,2,5]
for i in range(len(xiaohearrtest)):
    # print(xiaohearrtest[i])
    # print(i)
    pass


i=0
j=1
print(i,j)