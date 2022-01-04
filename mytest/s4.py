def megesortarr(merarr):

    if len(merarr) <= 1:
        return merarr
    mid = len(merarr)//2
    leftarr=megesortarr(merarr[:mid])
    print(megesortarr)
    rightarr=megesortarr(merarr[mid:])

    # leftarr=[1,2,3]
    # rightarr=[0, 4, 5]
    return merge(leftarr,rightarr)

def merge(leftarr,rightarr):
    helplist=[]
    # p1=L
    # p2=M+1
    j=h=0
    while(j<len(leftarr) and  h<len(rightarr)):
        # helplist[i+=1]=merarr[p1]<=merarr[p2] ? merarr[p1]:merarr[p1]
        if(leftarr[j]<rightarr[h]):
            helplist.append(leftarr[j])
            j+=1;
        else:
            helplist.append(rightarr[h])
            h+=1;
    while(j<len(leftarr)):
        # print(leftarr[j:])
        helplist=helplist+leftarr[j:]
        break
    while (h<=len(rightarr)):
        # print(rightarr[h:])
        helplist=helplist+rightarr[h:]
        break
    return helplist

# sortarr=[3,2,1,5,6,2]
sortarr=[4,5,3,8,1,6,9]
# sortarr=[3,2,1,4,5,0]
# sortarr=[3,2,1,4,5,0]
# sortarr=[4,5,0]
# sortarr=[3,1]
# sortarr=[1,2,3,4]

print((megesortarr(sortarr)))
# (megesortarr(0,len(sortarr)-1,sortarr))
# sortarr1=[1,2,3,2,5,6]