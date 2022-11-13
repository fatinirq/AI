# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 06:06:00 2022
8_Puzzle with DFS
@author: Fatin
"""



_close=[]
_open=[]
successors=[]
def generate(start):  
    indxBlank=start.index('blank')
    
    _temp=[]
    if (indxBlank in [2,5,8,1,4,7]):
        tempLeft=start.copy()
        tempLeft[indxBlank],tempLeft[indxBlank-1]=tempLeft[indxBlank-1],tempLeft[indxBlank]
        if(tempLeft not in _close and tempLeft not in _open):
            _temp.append(tempLeft)
   
    if (indxBlank in range(6)):
        tempDown=start.copy()
        tempDown[indxBlank],tempDown[indxBlank+3]=tempDown[indxBlank+3],tempDown[indxBlank]
        if(tempDown not in _close and tempDown not in _open):
            _temp.append(tempDown)
    if (indxBlank in [0,3,6,1,4,7]):
        tempRight=start.copy()
        
        tempRight[indxBlank],tempRight[indxBlank+1]=tempRight[indxBlank+1],tempRight[indxBlank]
        if(tempRight not in _close and tempRight not in _open):
            _temp.append(tempRight)
    if (indxBlank in range(3,9,1)):
        tempUp=start.copy()
        tempUp[indxBlank],tempUp[indxBlank-3]=tempUp[indxBlank-3],tempUp[indxBlank]
        if(tempUp not in _close and tempUp not in _open):
            _temp.append(tempUp)
    if(len(_temp)>0):
        return _temp
        
def getPathDepth(start,goal,_open,_close,paths,successors,limit):
  
    while True:
        # filtering success paths and its explored nodes
        level=0
        # Appending start in close list
        _close.append(start)
       
        for i,path in enumerate (paths):
            if path not in successors:
                if path[len(path)-1]==goal and start==goal:
                    successors.append({'index':len(successors),'path':path,'length':len(_close)})
                    
                elif path[-1]==start:
                    level=len(path)-1
        if level<=limit:
          
            newNodes=generate(start)
            
            
            if newNodes!=None :
        
               
        # adding new paths to the general list of paths
                for i,path in enumerate (paths):
                    if path[len(path)-1]==start:
                        for  i,node in enumerate(newNodes):
                            temp=path+[node]
                            paths.append(temp)
  
        # Merging open with list of children
                _open=_open+newNodes
        #print('paths ')
        #print("___________________________")
        #print(paths)
      
        if start==goal:
            print("successors", successors)
            print('Number of explored nodes=',len(_close))
            break
        elif  len(_open)==0:
            print('no path has been found')
            #print("paths",paths)
            break 
        else:
            start=_open[0]
            _close.append(start)
            _open.remove(start)


print('Call a')
print("start=[1,7,4,3,'blank',5,6,2,8]", "goal=[1, 'blank', 4,3, 7, 5, 2, 6, 8]")
print("__________________________________________________________________________")
getPathDepth([1,7,4,3,'blank',5,6,2,8],[1, 'blank', 4,3, 7, 5, 2, 6, 8],_open,_close,[[[1,7,4,3,'blank',5,6,2,8]]],successors,10)
print('Call b')
print("start=[1,'blank',7,4,3,5,6,2,8]", "goal=[1,2,3,4, 'blank',  5, 6, 7, 8]")
print("__________________________________________________________________________")
getPathDepth([1,'blank',7,4,3,5,6,2,8],[1,2,3,4, 'blank',  5, 6, 7, 8],_open,_close,[[[1,'blank',7,4,3,5,6,2,8]]],successors,10)
      
  

