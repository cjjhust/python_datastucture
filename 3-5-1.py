# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:01:07 2018

@author: CJJ
"""

class  BiTNode:
     def  __init__(self):
         self.data=None
         self.lchild=None
         self.rchild=None

"""
方法功能：判断两棵二叉树是否相等
参数：root1与root2分别为两棵二叉树的根结点
返回值：true:如果两棵树相等则返回true，否则返回false
"""
def  isEqual(root1,root2):
    if  root1==None and root2==None:
        return  True
    if  root1==None and root2!=None:
        return  False
    if  root1!=None and root2==None:
        return  False
    if  root1.data == root2.data:

        return  isEqual(root1.lchild,root2.lchild) and isEqual(root1.rchild,root2.rchild)
    else:
        return  False

def  constructTree():
        root=BiTNode()
        node1=BiTNode()
        node2=BiTNode()
        node3=BiTNode()
        node4=BiTNode()
        root.data=6
        node1.data=3
        node2.data=-7
        node3.data=-1
        node4.data=9
        root.lchild=node1
        root.rchild=node2
        node1.lchild=node3
        node1.rchild=node4
        node2.lchild=node2.rchild=node3.lchild=node3.rchild= \
        node4.lchild=node4.rchild=None
        return  root

if  __name__=="__main__": 
    root1=constructTree() 
    root2=constructTree()
    equal=isEqual(root1,root2)
    if  equal:
        print  "这两棵树相等"
    else:
        print  "这两棵树不相等"
