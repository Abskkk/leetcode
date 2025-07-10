'''
mono-decreasing stack
if we meet a temp larger than the top value in the stack
-> pop until stack is empty or temp <= top element
after iteration, days remain in stack will never meet a day larger than itself
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # [temp, day]
        stack = []
        res = [0] * n
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, day = stack.pop()
                res[day] = i - day
            stack.append([temp, i])
        
        return res
