class Solution:
    def romanToInt(self, s: str) -> int:
             arr = 0
             previous = 0
             map = { 'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
             for char in s[::-1]:
                 current = map[char]

                 if current < previous:
                      arr -= current

                 else:
                    arr += current 
                    previous = current


             return arr      