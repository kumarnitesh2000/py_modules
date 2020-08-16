def gfg(x,l=[]):
    print("before adding values to l  is : ",l)
    for i in range(x):
        l.append(i*i)
        print(l)

gfg(3)
gfg(3,l=[1,2])
gfg(2)
