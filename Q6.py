n,m,a,b,f,s,t = list(map(int, input().split())) # a,b: min,max n# of employees in a group       f,s,t max n of employees in a group from dep1,dep2,dep3
e = {} # employees: {name: [department, groupIndex], ...}
groups = []
d = {1: f, 2: s, 3: t}
for i in range(n):
    name, dep = input().split()
    e[name] = [int(dep), -1]
for i in range(m):
    x,y = input().split() # name1, name2 of employees who want to be together
    ix,iy = e[x],e[y] # informations about x,y
    dx,dy = ix[0],iy[0] # departments of x and y
    gx,gy = ix[1],iy[1] # groups of x and y
    if gx==-1 and gy==-1: # none of them has a group
        groups.append([x,y])
        groupIndex = len(groups)-1
        e[x][1],e[y][1] = groupIndex, groupIndex
    else:
        if gx!=-1 and gy==-1: #gx already has a group, can we add y into the same group?
            # i have to check:
            # 1. len(x group) has to be less than b
            # 2. the amount of employees from the same department as y is less then d[department of y]
            if len(groups[gx])<b and len([k for k in groups[gx] if e[k][1]==dy])<d[dy]:
                groups[gx].append(y)
                e[y][1] = gx
        elif gy!=-1 and gx==-1: #gy already has a group, can we add x into the same group?
            groupSize = len(groups[gy])<b
            depSize = len([k for k in groups[gy] if e[k][1]==dx])<d[dx]
            if groupSize and depSize:
                groups[gy].append(x)
                e[x][1] = gy
        elif gx!=-1 and gy!=-1 and gx!=gy:
            groupSize = len(groups[gy])+len(groups[gx])<=b
            depSize = True
            for ex_x in groups[gx]:
                ex_dx = e[ex_x][0]
                depSize = depSize & (len([k for k in groups[gx] if e[k][1]==ex_dx])+len([k for k in groups[gy] if e[k][1]==ex_dx]))<d[ex_dx]
            if groupSize and depSize:
                for ex_group_member in groups[gx]:
                    e[ex_group_member][1]=gy
                groups[gy].extend(groups[gx])
                groups[gx]=[]

biggest = []
for g in groups:
    if len(g)>len(biggest):
        biggest=g
biggest.sort()
print('\n'.join(biggest))