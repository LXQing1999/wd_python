"""
RedBlackTree 红黑树
Author:LXQing
Date:2023/7/12
"""

RED = 0
BLACK = 1


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = RED


def left_rotate(tree, node):
    if not node.right:
        return False
    node_right = node.right
    node_right.p = None
    # 如果node没有父亲,node是根,右旋有node_right是根
    if not node.p:  # 调整树根
        tree.root = node_right
    elif node == node.p.left:  # node是在父亲左孩子
        node.p.left = node_right
    else:
        node.p.right = node_right
    if node_right.left:
        node_right.left.p = node
    node.right = node_right.left
    node.p = node_right
    node_right.left = node


def right_rotate(tree, node):
    if not node.left:
        return False
    node_left = node.left
    node_left.p = node.p
    # 如果node没有父亲,node是根,右旋有node_right是根
    if not node.p:  # 调整树根
        tree.root = node_left
    elif node == node.p.right:  # node是在父亲左孩子
        node.p.right = node_left
    elif node == node_left.right:
        node.p.right = node_left
    if node_left.right:
        node_left.right.p = node
    node.left = node_left.right
    node.p = node_left
    node_left.right = node


class RedBlackTree:
    def __init__(self):
        self.root = None

    # 放入二叉排序树
    def insert(self, node: RedBlackTreeNode):
        if not self.root:
            self.root = node
        else:
            # current_node
            x = self.root
            while x:  # 当x为None时,y恰好是父亲
                y = x
                if node.value > x.value:
                    x = x.right
                else:
                    x = x.left
            node.p = y
            if node.value > y.value:
                y.right = node
            else:
                y.left = node
        self.insert_fixup(node)

    # 插入后的旋转
    def insert_fixup(self, node):
        parent: RedBlackTreeNode = node.p
        # 父亲存在而且父亲是红色
        while parent and parent.color == RED:
            grandpa: RedBlackTreeNode == parent.p
            grandpa = parent.p
            if parent == grandpa.left:
                uncle: RedBlackTreeNode = grandpa.right
                # 判断情形3
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandpa.color = RED
                    node = grandpa  # 爷爷重新作为node进行调整
                    parent = node.p
                    continue
                # 情形4
                if node == parent.right:
                    left_rotate(self, parent)
                    node, parent = parent, node
                # 情形5
                right_rotate(self, grandpa)
                parent.color = BLACK
                grandpa.color = RED
                break
            else:
                uncle: RedBlackTreeNode = grandpa.left
                # 判断情形3
                if uncle and uncle.color == RED:
                    parent.color = BLACK
                    uncle.color = BLACK
                    grandpa.color = RED
                    node = grandpa  # 爷爷重新作为node进行调整
                    parent = node.p
                    continue
                # 情形4
                if node == parent.left:
                    right_rotate(self, parent)
                    node, parent = parent, node
                # 情形5
                left_rotate(self, grandpa)
                parent.color = BLACK
                grandpa.color = RED
                break
        self.root.color = BLACK


def rbtree_print(node, key, direction):
    if node:
        if direction == 0:
            print("%2d(B) is root" % node.value)
        else:
            print("%2d(%s) is %2d's %6s child" % (
                node.value, ("B" if node.color == 1 else "R"), key, ("right" if direction == 1 else "left")
            ))
        rbtree_print(node.left, node.value, -1)
        rbtree_print(node.right, node.value, 1)


def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    tree = RedBlackTree()
    for number in number_list:
        node = RedBlackTreeNode(number)
        tree.insert(node)
        del node
    rbtree_print(tree.root, tree.root.value, 0)

if __name__ == '__main__':
    main()

        # a = [1, 2, 3]
        # b = a
        # del a
        # print('引用＋1,硬链接', b)

