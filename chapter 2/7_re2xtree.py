# coding = utf-8
# 重建二叉树

qian = [1,2,4,7,3,5,6,8]
zhong = [4,7,2,1,5,3,8,6]


class BinaryTreeNode(object):
    def __init__(self,_x):
        self.x = _x
        self.left = None
        self.right = None

def build1layer(preorder, innerorder, root):
    if root == None:
        return None
    prei = preorder.index(root.x)
    inni = innerorder.index(root.x)
    
    for i in range(prei+1,len(preorder)):
        print('------------',i)
        # 左子树
        if preorder[i] in innerorder and innerorder.index(preorder[i]) < inni and root.left == None:
            root.left = BinaryTreeNode(preorder[i])
        # 右子树
        if preorder[i] in innerorder and innerorder.index(preorder[i]) > inni and root.right == None:
            root.right = BinaryTreeNode(preorder[i])
        if root.left and root.right:
            break

    # 递归构造具体的左右子树
    if len(innerorder[:inni]) != 0:
        root.left = build1layer(preorder, innerorder[:inni], root.left)
    if len(innerorder[inni:]) != 0:
        root.right = build1layer(preorder, innerorder[inni:], root.right)

    return root


root = BinaryTreeNode(qian[0])
root = build1layer(qian, zhong, root)
print('------over------')
'''
# 遍历打印二叉树
temp = [root]
while temp:
    print(temp[0].x)
    if temp[0].left:
        temp.append(temp[0].left)
    if temp[0].right:
        temp.append(temp[0].right)
    temp = temp[1:]



    
