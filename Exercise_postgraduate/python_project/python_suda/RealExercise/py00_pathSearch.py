# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:47:15 2020

@author: douzi
"""

def searchPath(graph, start, end):
    
    results = []
    
    _generatePath(graph, [start], end, results)
    
    # 按 所有路径的长度排序
    results.sort(key=lambda x:len(x))
    return results


def _generatePath(graph, path, end, results):
    current = path[-1]
    print(current)
    # 遇到 end 的时候         
    if current == end:               
        results.append(path)        
    else:
        for n in graph[current]: 
            if n not in path:     
                _generatePath(graph, path + [n], end, results)
            
def showPath(results):
    print("The path from ", results[0][0], ' to ', results[0][-1], ' is:')
    
    for path in results:
        print(path)
        
        
if __name__=='__main__':
    graph = {'A' : ['B', 'C', 'D'],
             'B' : ['E'], 
             'C' : ['B', 'E', 'G'],
             'E' : ['D'],
             'F' : ['D', 'G'],
             'G' : ['E']}
    
    r1 = searchPath(graph, 'A', 'D')
    
    showPath(r1)
    
    