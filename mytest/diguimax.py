



def nixuduiarr(nxdarr):
    for i in range(len(nxdarr)-1):
        for j in range(i+1,len(nxdarr)):
            if(nxdarr[j]<nxdarr[i]):
                print(nxdarr[i],nxdarr[j])
nxdarrtest=[3,2,4,5,0]

(nixuduiarr(nxdarrtest))