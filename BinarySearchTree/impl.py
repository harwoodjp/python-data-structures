class Node(object):
	def __init__(self, data=None, left_child=None, right_child=None):
		self.data = data
		self.left_child = left_child
		self.right_child = right_child

class BST(object):
	def __init__(self, root=None):
		self.root = root

	def insert(self, data):
		new_node = Node(data)
		if self.root is None:
			self.root = new_node
		else:
			self.search_and_insert(self.root, new_node)
	
	def search_and_insert(self, current_node, new_node):
		if current_node.data >= new_node.data:
			if current_node.left_child:
				self.search_and_insert(current_node.left_child, new_node)
			else:
				current_node.left_child = new_node
		elif current_node.data <= new_node.data:
			if current_node.right_child:
				self.search_and_insert(current_node.right_child, new_node)
			else:
				current_node.right_child = new_node


def main():
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


main()