# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:40:47 2018

@author: Administrator
"""

import  math
def  radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[]  for  i  in  range(radix)]
    for  i  in  range(1, k+1):
        for  j  in  lists:
            bucket[int(j/(radix**(i-1))) % (radix)].append(j)
        del lists[:]
        for  z  in  bucket:
            lists += z
            del z[:]
    return  lists

if  __name__=="__main__":  
    lists=[31,43,25,83,98,55,14,100]
    print('排序前序列为:')
    for  i  in  lists:
        print  (i)
    print  ('\n排序后结果为:') 
    for  i  in  (radix_sort(lists)):
        print (i)
