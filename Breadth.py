# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 06:06:00 2022

@author: Fatin
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:30:12 2021

@author: Fatin
"""
arcs={'a':['b','c','d'],'b':['d','e','f'],'c':['g','h']
     ,'d':['i']
     ,'e':['l']
     ,'h':['o','p']
     ,'i':['p','q']
     ,'j':['r']
     ,'k':['s']
     ,'l':['t']
     ,'p':['u']}

_close=[]
_open=[]
successors=[]
def getPathBreadth(start,goal,_open,_close,paths,successors):
    # Filtering success paths and its explored nodes
    if start==goal:
        for i,path in enumerate (paths):
            if path not in successors:
                if path[len(path)-1]==goal:
                    successors.append({'index':len(successors),'path':path,'length':len(_close)})
    newNodes=arcs.get(start)
    _temp=[]
    if newNodes!=None:
# Appending start in close list
        _close.append(start)
# Adding new paths to the general list of paths
        for i,path in enumerate (paths):
            if path[len(path)-1]==start:
                for  i,node in enumerate(newNodes):
                    temp=path+[node]
                    paths.append(temp)
# Comparing new chiledren with open and close lists       
        for  i,node in enumerate (newNodes) :
            if node not in _open and node not in _close:
                _temp.append(node)
# Merging open with the list of children
    _open=_temp+_open
    
    if len(_open)==0:
        print(successors)
        return 
    else:
        start=_open[0]
        _open.remove(start)
        getPathBreadth(start,goal,_open,_close,paths,successors)
    
getPathBreadth('a','h',_open,_close,[['a']],successors)  
        
  

