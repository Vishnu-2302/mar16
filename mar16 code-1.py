x=input()
l=[]
[l.append(i) for i in x if i not in l]
l=[print(i,end='') for i in l]