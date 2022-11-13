# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:09:41 2021
7_Bridges  of Königsberg representation
@author: Fatin
"""


connect={'i1':[['b1','i2'],['b2','rb1'],['b3','rb1'],['b5','rb2'],['b6','rb2']],
         'i2':[['b1','i2'],['b4','rb1'],['b7','rb2']],
         'rb1':[['b2','i1'],['b3','i1'],['b4','i2']],
         'rb2':[['b5','i1'],['b6','i1'],['b7','i2']]}

print (connect['i1'])
print (connect['i1'][0])
print (connect['i1'][0][1])

Keys = connect.keys()
print(Keys)

Values= connect.values()
print(Values)
#Values
for v in connect.values():
    print(v)
#Keys
for k in connect.keys():
    print ('key=',k)
#Items
for item in connect:
    print('item=',item)
for item in connect.items():
    print('item2=',item)
    print('item 2 value', item[1])

print ('connect', connect)

