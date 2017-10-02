#
#    A Binary Search Tree is a tree sorted s.t. a node's left child is greater and right child smaller than itself
#         (4)
#	    /    \
#     (2)    (6)
#       \    /  \
#       (3) (5) (9)
#

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