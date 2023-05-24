a = [1]*5
setsArr = []
costdict = {0:10, 1:5, 2:10, 3:20, 4:40, 5:1}
for i in range(6**5+1):
    setsArr.append(a[:])
    a[-1] += 1
    for j in range(4,-1,-1):
        if j:
            a[j-1]+=(a[j]-1)//6
        if(a[j]==7):
            a[j]=1

def V(a):
    b = list(a)
    b.sort()
    # 5 same
    if(b[0]==b[1] and b[1]==b[2] and b[2]==b[3] and b[3]==b[4]):
        return b[0]*5*0.1
    # 4 same
    if(b[0]==b[1] and b[1]==b[2] and b[2]==b[3]) or (b[1]==b[2] and b[2]==b[3] and b[3]==b[4]):
        return b[2]*4*0.01
    # fullhouse
    if(b[0]==b[1] and b[1]==b[2] and b[3]==b[4]) or (b[0]==b[1] and b[2]==b[3] and b[3]==b[4]):
        return sum(b)*0.01
    if(b[0]+1==b[1] and b[1]+1==b[2] and b[2]+1==b[3] and b[3]+1==b[4]):
        return sum(b)*0.01
    return 0

def issubset(a,b):
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return False
    return True

def lock(locked):
    locked = locked[:]
    locked.sort()
    possibleSets = []
    for sets in setsArr:
        if(issubset(locked, sets)):
            possibleSets.append(sets)
    
    E = 0
    for sets in possibleSets:
        E += V(sets)
    return E/len(possibleSets)

d = {}
def enumerate_combinations(points):
    def backtrack(index, current_combination):
        if index == len(points):
            # 到達終止條件，輸出當前組合
            E = lock(current_combination)/costdict[len(current_combination)]
            # print(f'Sets {current_combination}: {E}')
            if(E not in d):
                d[E] = set()
            d[E].add(str(current_combination))
            
        else:
            # 選擇當前點數
            current_combination.append(points[index])
            backtrack(index + 1, current_combination)
            
            # 不選擇當前點數
            current_combination.pop()
            backtrack(index + 1, current_combination)
    
    current_combination = []
    backtrack(0, current_combination)

if __name__ == '__main__':
    """
    a = [4]
    print(lock(a))
    """
    while(True):
        print("-")
        mySets = [int(x) for x in input()]
        if(len(mySets)!=5):
            continue
        enumerate_combinations(mySets)
        sorted_items = sorted(d.items())
        f = open('test.txt', 'w')
        for key,val in sorted_items:
            print(f'{key:.6f}: {val}', file=f)
        f.close()
        d = {}
    #"""