# The updateMatrix method updates a binary matrix so that each cell containing 1 is replaced by its distance to the nearest 0.

# Step 1: Initialization
#   - If the matrix is empty, return an empty list.
#   - Store matrix dimensions (m, n) and initialize a queue for BFS.
#   - Mark cells with 1 as unvisited (set to a large value) and add cells with 0 to the queue.

# Step 2: BFS
#   - Define directions (up, down, left, right) for neighbor traversal.
#   - While the queue is not empty:
#       - Dequeue a cell and process its neighbors.
#       - If a neighbor's value is greater than the current cell's value + 1, update it and add it to the queue.

# Step 3: Return Result
#   - Return the updated matrix with the shortest distances to the nearest 0.

# TC: O(m * n) - Each cell is processed once during BFS.
# SC: O(m * n) - Space for the queue and updated matrix values.


from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX_VALUE = m * n
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1
        
        return mat