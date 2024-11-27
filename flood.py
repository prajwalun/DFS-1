# The floodFill method performs a flood fill on an image starting from a given pixel (sr, sc) and replaces all connected pixels of the same color with a new color.

# Step 1: Initialization
#   - Store the starting pixel's color as 'start_color'.
#   - If the starting pixel already has the new color, return the image immediately (handled in recursion).

# Step 2: Recursive Flood Fill
#   - Define a helper function flood_fill(x, y) to perform the fill:
#       - If the current pixel is out of bounds, return.
#       - If the pixel's color is already the new color or does not match the start color, return.
#       - Update the current pixel's color to the new color.
#       - Recursively call flood_fill for the four neighboring pixels (up, down, left, right).

# Step 3: Start Flood Fill
#   - Call flood_fill on the starting pixel (sr, sc).
#   - Return the updated image.

# TC: O(m * n) - Each pixel is visited at most once.
# SC: O(m * n) - Space for the recursion stack in the worst case.


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        start_color = image[sr][sc]
        
        def flood_fill(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != start_color: return
            
            image[x][y] = color
            
            flood_fill(x-1, y)
            flood_fill(x+1, y)
            flood_fill(x, y+1)
            flood_fill(x, y-1)
        
        flood_fill(sr, sc)
        return image