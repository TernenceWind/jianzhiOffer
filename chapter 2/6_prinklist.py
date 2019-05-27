# coding = utf-8
# 单链表的倒叙输出


class Node(object):
    def __init__(self, x):
        self.x = x
        self.next = None
thenext = None
link = None
strs = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(len(strs)):
    link = Node(strs[i])
    link.next = thenext
    thenext = link

# 1 利用栈
def stackprint(link):
    stack = []
    while link.next != None:
        stack.append(link.x)
        link = link.next
    stack.append(link.x)
    while stack:
        print(stack.pop())

#stackprint(link)

# 利用递归
def recursionprint(link):
    if link.next != None:
        recursionprint(link.next)
    print(link.x)
    return
recursionprint(link)