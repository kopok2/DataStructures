# coding=utf-8
"""Red-Black Tree Python implementation."""


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = "RED"

    def uncle(self):
        if not self.parent:
            return None
        elif not self.parent.parent:
            return None
        elif self.parent.is_on_left():
            return self.parent.parent.right
        else:
            return self.parent.parent.left

    def is_on_left(self):
        return self == self.parent.is_on_left

    def sibling(self):
        if not self.parent:
            return None
        elif self.is_on_left():
            return self.parent.right
        else:
            return self.parent.left

    def move_down(self, nparent):
        if self.parent:
            if self.is_on_left():
                self.parent.left = nparent
            else:
                self.parent.right = nparent
            nparent.parent = self.parent
            self.parent = nparent

    def has_red_child(self):
        has = False
        if self.left:
            if self.left.color == "RED":
                has = True
        if self.right:
            if self.right.color == "RED":
                has = True
        return has


class RedBlackTree:
    def __init__(self):
        self.root = None

    def left_rotate(self, x):
        nparent = x.right
        if x == self.root:
            self.root = nparent
        x.move_down(nparent)
        x.right = nparent.left
        if nparent.left:
            nparent.left.parent = x
        nparent.left = x

    def right_rotate(self, x):
        nparent = x.left
        if x == self.root:
            self.root = nparent
        x.move_down(nparent)
        x.left = nparent.right
        if nparent.right:
            nparent.right.parent = x
        nparent.right = x

    def swap_colors(self, x1, x2):
        x1.color, x2.color = x2.color, x1.color

    def swap_values(self, x1, x2):
        x1.val, x2.val = x2.val, x1.val

    def fix_red_red(self, x):
        if x == self.root:
            x.color = "BLACK"
            return None
        parent = x.parent
        grandparent = parent.parent
        uncle = x.uncle()
        if parent.color != "BLACK":
            if uncle:
                if uncle.color == "RED":
                    parent.color = "BLACK"
                    uncle.color = "BLACK"
                    grandparent.color = "RED"
                    self.fix_red_red(grandparent)
            else:
                if parent.is_on_left():
                    if x.is_on_left():
                        self.swap_colors(parent, grandparent)
                    else:
                        self.left_rotate(parent)
                        self.swap_colors(x, grandparent)
                    self.right_rotate(grandparent)
                else:
                    if x.is_on_left():
                        self.right_rotate(parent)
                        self.swap_colors(x, grandparent)
                    else:
                        self.swap_colors(parent, grandparent)
                    self.left_rotate(grandparent)

    def successor(self, x):
        tmp = x
        while tmp.left:
            tmp = tmp.left
        return tmp

    def bst_replace(self, x):
        if x.left and x.right:
            return self.successor(x.right)
        if not x.left and not x.right:
            return None
        if x.left:
            return x.left
        else:
            return x.right

    def delete_node(self, v):
        u = self.bst_replace(v)
        uvblack = ((u == None or u.color == "BLACK") and (v.color == "BLACK"))
        parent = v.parent
        if not u:
            if v == self.root:
                self.root = None
            else:
                if uvblack:
                    self.fix_double_black(v)
                else:
                    if v.sibling():
                        v.sibling().color = "RED"
                if v.is_on_left():
                    parent.left = None
                else:
                    parent.right = None
            return None

        if not v.left or not v.right:
            if v == self.root:
                v.val = u.val
                v.left = None
                v.right = None
            else:
                if v.is_on_left():
                    parent.left = u
                else:
                    parent.right = u
                u.parent = parent
                if uvblack:
                    self.fix_double_black(u)
                else:
                    u.color = "BLACK"
            return None
        self.swap_values(u, v)
        self.delete_node(u)

    def fix_double_black(self, x):
        if x == self.root:
            return None
        sibling = x.sibling()
        parent = x.parent
        if not sibling:
            self.fix_double_black(parent)
        else:
            if sibling.color == "RED":
                parent.color = "RED"
                sibling.color = "BLACK"
                if sibling.is_on_left():
                    self.right_rotate(parent)
                else:
                    self.left_rotate(parent)
                self.fix_double_black(x)
            else:
                if sibling.has_red_child():
                    if sibling.left:
                        if sibling.left.color == "RED":
                            if sibling.is_on_left():
                                sibling.left.color = sibling.color
                                sibling.color = parent.color
                                self.right_rotate(parent)
                            else:
                                sibling.left.color = parent.color
                                self.right_rotate(sibling)
                                self.left_rotate(parent)
                    else:
                        if sibling.is_on_left():
                            sibling.right.color = parent.color
                            self.left_rotate(sibling)
                            self.right_rotate(parent)
                        else:
                            sibling.right.color = sibling.color
                            sibling.color = parent.color
                            self.left_rotate(parent)
                    parent.color = "BLACK"
                else:
                    sibling.color = "RED"
                    if parent.color == "BLACK":
                        self.fix_double_black(parent)
                    else:
                        parent.color = "BLACK"

    def level_order(self, x):
        if not x:
            return None
        q = []
        q.append(x)
        while q:
            curr = q.pop(0)
            print(curr.val, end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    def inorder(self, x):
        if not x:
            return None
        self.inorder(x.left)
        print(x.val, end=" ")
        self.inorder(x.right)

    def search(self, n):
        tmp = self.root
        while tmp:
            if n < tmp.val:
                if not tmp.left:
                    break
                else:
                    tmp = tmp.left
            elif n == tmp.val:
                break
            else:
                if not tmp.right:
                    break
                else:
                    tmp = tmp.right
        return tmp

    def insert(self, n):
        newnode = Node(n)
        if not self.root:
            newnode.color = "BLACK"
            self.root = newnode
        else:
            tmp = self.search(n)
            if tmp.val == n:
                return None
            newnode.parent = tmp
            if n < tmp.val:
                tmp.left = newnode
            else:
                tmp.right = newnode
            self.fix_red_red(newnode)

    def delete_by_val(self, n):
        if not self.root:
            return None
        v = self.search(n)
        if v.val != n:
            print("No n in tree")
            return
        self.delete_node(v)

    def print_in_order(self):
        print("INORDER")
        self.inorder(self.root)

    def print_level_order(self):
        print("LEVELORDER")
        self.level_order(self.root)


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(7)
    tree.insert(3)
    tree.insert(18)
    tree.insert(10)
    tree.insert(22)
    tree.insert(8)
    tree.insert(11)
    tree.insert(26)
    tree.insert(2)
    tree.insert(6)
    tree.insert(13)

    tree.print_in_order()
    tree.print_level_order()

    print("Deleting 18, 11, 3, 10, 22")

    tree.delete_by_val(18)
    tree.delete_by_val(11)
    tree.delete_by_val(3)
    tree.delete_by_val(10)
    tree.delete_by_val(22)

    tree.print_in_order()
    tree.print_level_order()
