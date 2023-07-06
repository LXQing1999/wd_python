"""
complete_BT 完全二叉树
Author:LXQing
Date:2023/7/4
"""


class Node(object):  # 建一个新结点
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    # 新建根结点和空队列
    def __init__(self):
        self.root = None
        self.queue = []

    def insert_node(self, elem):
        new_node = Node(elem)
        self.queue.append(new_node)  # 放入队列
        if self.root is None:
            self.root = new_node  # 树为空 new_node为根节点
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = new_node
            elif self.queue[0].rchild is None:
                self.queue[0].rchild = new_node
                self.queue.pop(0)  # 出队

    def preorder(self, current_node: Node):
        if current_node:
            print(current_node.elem, end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def midorder(self, current_node: Node):
        if current_node:
            self.midorder(current_node.lchild)
            print(current_node.elem, end=' ')
            self.midorder(current_node.rchild)

    def postorder(self, current_node: Node):
        if current_node:
            self.postorder(current_node.lchild)
            self.postorder(current_node.rchild)
            print(current_node.elem, end=' ')


if __name__ == '__main__':
    completeBT = Tree()
    for i in range(1, 16):
        completeBT.insert_node(i)
    completeBT.preorder(completeBT.root)
    print('\n')
    completeBT.midorder(completeBT.root)
    print('\n')
    completeBT.postorder(completeBT.root)
    print('\n')
