# https://www.hackerrank.com/challenges/saveprincess?hr_b=1

#!/usr/bin/python

import time
def pos(n,grid,c):
    pos=[]
    for i in range(n):
        for j in range(n):
            if(grid[i][j]==c):
                pos.append(i)
                pos.append(j)
                break
    return pos
def displayPathtoPrincess(n,grid):
    p_pos=pos(n,grid,"p")
    m_pos=pos(n,grid,"m")
    while(m_pos[0]!=p_pos[0] or m_pos[1]!=p_pos[1]):
        if(m_pos[0]<p_pos[0]):
            print("DOWN")
            m_pos[0]=m_pos[0]+1
        if(m_pos[0]>p_pos[0]):
            print("UP")
            m_pos[0]=m_pos[0]-1
        if(m_pos[1]>p_pos[1]):
            print("LEFT")
            m_pos[1]=m_pos[1]-1
        if(m_pos[1]<p_pos[1]):
            print("RIGHT")
            m_pos[1]=m_pos[1]+1
m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())
start=time.time()
displayPathtoPrincess(m,grid)
end=time.time()
print(end-start)
