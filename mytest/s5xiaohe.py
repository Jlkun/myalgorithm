"""
小和问题，递归解法
"""

class xiaohe():
    def xiaohearrjy(self,xharr):
        if(len(xharr)<2):
            return 0
        return self.xiaohearr(xharr,0,len(xharr)-1)

    def xiaohearr(self,xarr,L,R):
        if L==R:
            return 0
        mid =L+(R-L)//2
        leftarr=self.xiaohearr(xarr,L,mid)
        rightarr=self.xiaohearr(xarr,mid+1,R)
        return leftarr+rightarr+self.merge(xarr,L,mid+1,R)

    def merge(self,xarr,L,mid,R):
        helplist=[]
        arrmun=0
        p1=L
        p2=mid
        while(p1<=mid and p2 <=R):
            arrmun+=xarr[p1]*(R-p2+1) if  xarr[p1]<xarr[p2] else 0
            if(xarr[p1]<xarr[p2]):
                helplist.append(xarr[p1])
                p1+=1
            else:
                helplist.append(xarr[p2])
                p2 += 1

        while(p1<=mid):
            helplist.append(xarr[p1])
            p1 += 1
        while (p2 <=R):
            helplist.append(xarr[p2])
            p2 += 1
        xarr[L:R+1]=helplist  #对数组进行排序
        return arrmun

if __name__ == '__main__':
    li = [1,3,4,2,5]
    ss = xiaohe()

    sum = ss.xiaohearrjy(li)
    print(sum)



# # coding=utf8
#
# class Small_Sum():
#     def small_sums(self, li):
#         """当为空或者长度小于2是返回0"""
#         if li is None or len(li) < 2:
#             return 0
#         return self.small_sum(li, 0, len(li) - 1)
#
#
# # 进行递归的函数
#     def small_sum(self, li, l, r):
#         if l == r:
#             return 0
#         mid = l + ((r - l) // 2)
#
#         return self.small_sum(li, l, mid) + self.small_sum(li, mid + 1, r) + self.merge(li, l, mid, r)
#         # 找出小和与排序
#
#
#     def merge(self, li, l, mid, r):
#         res = 0
#         help = []  # 定义临时列表来暂时存储元素
#         p1 = l
#         p2 = mid + 1
#         while p1 <= mid and p2 <= r:
#             res += (r - p2 + 1) * li[p1] if li[p1] < li[p2] else 0
#             if li[p1] < li[p2]:
#                 help.append(li[p1])
#                 p1 += 1
#             else:
#                 help.append(li[p2])
#                 p2 += 1
#         # 两个循环只能进去一个
#         while p1 <= mid:
#             help.append(li[p1])
#             p1 += 1
#
#         while p2 <= r:
#             help.append(li[p2])
#             p2 += 1
#         li[l:r + 1] = help
#         return res  # 返回小和
#
#
# if __name__ == '__main__':
#     li = [1,3,4,2,5]
#     ss = Small_Sum()
#
#     sum = ss.small_sums(li)
#     print(sum)
