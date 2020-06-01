# -*- coding: utf-8 -*-

class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        forward = 0
        backward = 0 
        dlen = len(distance)
        
        for i in range(0, dlen):
            forward += distance[(start + i) % dlen]
            if (start + i + 1) % dlen == destination:
                break
            
        for i in range(0, dlen):
            backward += distance[(start + dlen - i - 1) % dlen]
            if (start + dlen - i - 1) % dlen == destination:
                break
        
#        print(forward, backward)
        return forward if forward < backward else backward
                

s = Solution()

print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 1))

print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))
