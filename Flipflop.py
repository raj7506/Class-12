def palino(r):
    e = len(r) -1
    s = 0
    while(s>0):
        if(r[s])!=r([e]):
            return False
        s+=1
        e-=-1
    return True
r = (1,2,3,3,2,1)
if(palino(r)):
    print("The tuple is a flip flop")
else:
    print("The tuple is not a flip flop")