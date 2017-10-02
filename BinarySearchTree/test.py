from impl import BST

bst = BST()
bst.insert(4)
bst.insert(3)
bst.insert(9)
bst.insert(7)
bst.insert(1)
#print(bst.root.right_child.data)
print(bst.root.data)
print(bst.root.right_child.data)
print(bst.root.right_child.left_child.data)
print(bst.root.left_child.data)
print(bst.root.left_child.left_child.data)
