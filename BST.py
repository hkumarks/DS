root=None

class Node:
    def __init__(self,key):
        self.key=key
        self.left=self.right=None

def insert(root,key):
    if root is None:
        return Node(key)

    if root.key>key:
        root.left=insert(root.left,key)              
    else:
        root.right=insert(root.right,key)

    return root    

def delete(root,key):
    if root is None:
        return root
    if root.key>key:
        root.left=delete(root.left,key)
    elif root.key<key:
        root.right=delete(root.right,key)

    else:
        if root.left is None and root.right==None:
            return None
        elif root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        else:
            cur=root.right
            while cur.left is not None:
                cur=cur.left
            root.key=cur.key
            root.right=delete(root.right,cur.key)
    return root                       


def traversal(root):
    if root is not None:
        traversal(root.left)
        print(root.key,end=' ')
        traversal(root.right)

root=insert(root,11)
root=insert(root,3)
root=insert(root,20)
root=insert(root,19)
traversal(root)
print()
root=delete(root,20)
root=delete(root,11)
traversal(root)
print()
root=insert(root,14)
traversal(root)


