class Solution:
   # def dfs(self,currR, currC, grid: List[List[str]], visited: set) -> tuple(int, set):
    def dfs(self,currR, currC, grid: List[List[str]], visited: set) -> int:
        direction=[(0,1),(1,0),(-1,0),(0,-1)] 
        visited.add((currR,currC))  
        for r,c in direction:
            newR = currR + r
            newC = currC + c
            if newR>=0 and newC>=0 and newR<len(grid) and newC<len(grid[0]) and (newR, newC) not in visited and grid[newR][newC]=="1": 
                self.dfs(newR, newC, grid, visited)
            else:
                continue
        #return 1, visited 
        return visited

        #so it will start on node, and go to all nubmers and see if valid, if valid then run dfs on it
        # and it will explroe the 4 directiosn on each of those 4 neighbor directions, and add those to the visited, but if that is done it wil lreturn visited,  which since it was called by a parent cal lwill give the parent call the visited right or whatever, but since theres 4 parallel calls chidl calls from the original call on currr currc, will the nodes they vsiited their edited visited array be used by the other child calls or no i guess its not concerning if they dont because either way through their collaborative effort all the island ndoes will be marked as visited in the visited and that is returned to numislands and counted as 1 right...i'm trying to still logic and jsutify why dfs is necessary rather than somethign else nondfs
        

    def numIslands(self, grid: List[List[str]]) -> int:
        count =0
        visited=set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and (row, col) not in visited: 
                    count+=1
                    visited = self.dfs(row, col, grid, visited)
                    #thing, visited=self.dfs(row, col, grid, visited)
                    #count+=thing
        return count

