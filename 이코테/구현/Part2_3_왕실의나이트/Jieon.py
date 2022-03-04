
data=str(input())
row=data[1]
column=data[0]
init=(ord(column)-ord('a')+1,int(row))

r1_x=[2,-2]
r1_y=[1,-1]
r2_x=r1_y
r2_y=r1_x

result=0
for i in range(2):
    for j in range(2):
        #rule1
        x=init[0]+r1_x[i]
        y=init[1]+r1_y[j]
        if (x>0 and x<=8) and (y>0 and y<=8):
            result+=1
        #rule2
        x=init[0]+r2_x[i]
        y=init[0]+r2_y[j]
        if (x>0 and x<=8) and (y>0 and y<8):
            result+=1
print(result)
