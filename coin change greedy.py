def coin(A,t):
    c=0
    A_new=sorted(A)
    while t!=0:
        m_v=A_new[-1]
        if t>=m_v:
            c+=1
            t=t-m_v
        else:
            A_new.pop()
    return c

A={1,2,5,10,20,50,100,1000}
t=200
print(coin(A,t))       

