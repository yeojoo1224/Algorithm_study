from uuid import NAMESPACE_X500


n=int(input())
uglys=[0]*n
n2=2
n3=3
n5=5
i2=i3=i5=0
uglys[0]=1
for i in range(1,n):
    uglys[i]=min(n2,n3,n5)
    if uglys[i]==n2:
        i2+=1
        n2=uglys[i2]*2
    if uglys[i]==n3:
        i3+=1
        n3=uglys[i3]*3
    if uglys[i]==n5:
        i5+=1
        n5=uglys[i5]*5

print(uglys[n-1])

#답지참조