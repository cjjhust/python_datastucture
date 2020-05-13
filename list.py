#!python3
#实现链表逆序，head>1>2>3>4>5变为5>4>3>2>1>head
#含头结点
#2020-4-30 by CJJ

class LNode:
    def __init__(self,x):
        self.data=x
        self.next=None

#创建链表1~8
i=1
head=LNode(-1)
head.next=None
tmp=None
cur=head
while i<8:
    tmp=LNode(i)
    cur.next=tmp
    cur=tmp
    i+=1
    

def print_list(head):
    cur=head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next

print("逆序前：")
print_list(head)


#递归逆序
'''
首先对不带头结点的单链表逆序
输入参数：head表示第一个结点
'''

def Reverse_without_head(head):
    if head is None or head.next is None:
        return head
    else:
        newhead=Reverse_without_head(head.next)
        head.next.next=head
        head.next=None
    return newhead


'''
方法：对带head头结点进行逆序，引用Reverse_without_head函数
输入参数：head头结点
'''

def Reverse(head):
    if head is None:
        return
    firstnode=head.next
    newhead=Reverse_without_head(firstnode)
    head.next=newhead

print(head.data)
newhead=Reverse(head)
print("逆序后：")
print_list(head)
