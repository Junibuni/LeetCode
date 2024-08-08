class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        r, c = rStart, cStart
        output = [[r, c]]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        length = 1
        direction_idx = 0
        
        while len(output) < (rows * cols):
            for _ in range(2):
                for _ in range(length):
                    dr, dc = directions[direction_idx]
                    r += dr
                    c += dc
                    
                    if r < rows and c < cols and 0 <= r and 0 <= c:
                        output.append([r, c])
                direction_idx = (direction_idx + 1) % 4
            length += 1
        
        return output
                