from numpy import *
class Solution:

# method 1
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:        
        m=len(grid)  # rows
        n=len(grid[0]) # columns
        k_index=0        
        if k==0:
            return grid 

        while k_index<k:
        
            ans=full((m,n),0)
            for i in range(m):
                for j in range(n):
                    if i<=m-1 and j<n-1:
                        ans[i][j+1]=grid[i][j]
                    elif i<m-1 and j==n-1:
                        ans[i+1][0]=grid[i][j]
                    elif i==m-1 and j==n-1:
                        ans[0][0]=grid[i][j]            
            grid=ans
            k_index+=1
            
        return ans

# method 2: this is simple
        m,n=len(grid),len(grid[0])

        for _ in range(k):
            previous_element=grid[-1][-1]             
            for i in range(m):
                for j in range(n):
                    tomove=grid[i][j]
                    grid[i][j]=previous_element
                    previous_element=tomove
        return grid
