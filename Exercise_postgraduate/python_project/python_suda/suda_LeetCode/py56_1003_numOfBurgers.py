# -*- coding: utf-8 -*-
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        
        low, high = 0, tomatoSlices // 4
        
#        巨无霸汉堡：4 片番茄和 1 片奶酪
#        小皇堡：2 片番茄和 1 片奶酪
        print(low, high)
        
        while low <= high:
            mid = (low + high) // 2   # 巨无霸数量
            tomatos, cheeses = tomatoSlices - mid*4, cheeseSlices - mid
            
            # 符合 小皇煲 的 数据比
            if tomatos == cheeses*2:        
                return [mid, cheeses]   
            elif tomatos > cheeses*2:
                low = mid + 1
            else:
                high = mid - 1
        return []


s = Solution()
#print(s.numOfBurgers(tomatoSlices = 48, cheeseSlices = 16))
print(s.numOfBurgers(tomatoSlices = 16, cheeseSlices = 7))
#print(s.numOfBurgers(tomatoSlices = 17, cheeseSlices = 4)) 
#print(s.numOfBurgers(tomatoSlices = 0, cheeseSlices = 0)) 
        
        
        
        
