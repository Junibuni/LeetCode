class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0 for i in range(n)]
        
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)
        
        return output
            
                