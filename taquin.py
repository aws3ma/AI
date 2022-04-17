# l = [1,4,3,0,5,6,7,8,9,11,15,16,20,30,40,50]
l = [1,4,3,0,5,6,7,8,9]
j=0
m = []
b = []
n=3
for k in l:
    if j<n:
        m.append(k)
        j+=1
    if j==n:
        b.append(m)
        m=[]
        j=0
print(b)




def zero_pos(b,n):
    i=0
    j=0
    while i<n:
        while j<n:
            print(b[i][j])
            if b[i][j]==0:
                return (i,j)
            j+=1
        j=0
        i+=1
    return (-1,-1)
m=zero_pos(b,n)
print(m)
def generate_possibilities(m,n):
    pos=[]
    l=[]
    # for i in range(n):
    if m[0]>0:
        l.append(m[0]-1)
        l.append(m[1])
        pos.append(l)
        l=[]
    if m[0]<n:
        l.append(m[0]+1)
        l.append(m[1])
        pos.append(l)
        l=[]
    if m[1]>0:
        l.append(m[0])
        l.append(m[1]-1)
        pos.append(l)
        l=[]
    if m[1]<n:
        l.append(m[1]+1)
        l.append(m[0])
        pos.append(l)
        l=[]

    return pos

pos=generate_possibilities(m,n-1)
print(pos)

