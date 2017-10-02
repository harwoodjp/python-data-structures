#
#    A singly-linked list is a chain of nodes linked with pointers
#    |1, next=2| -> |2, next=3| -> |3, next=5| -> |5, next=null|
#

class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head
	def delete(self, data): 
		tmp_head = self.head
		last_node = None
		while (tmp_head):
			if (tmp_head.data == data):
				if (tmp_head.next):
					if (last_node):
						last_node.next = tmp_head.next
					else:
						self.head = tmp_head.next
				else: 
					last_node.next = None
			last_node = tmp_head
			tmp_head = tmp_head.next
	def insert(self, data):
		new_node = Node(data, self.head)
		self.head = new_node
	def print(self):
		tmp_head = self.head
		while (tmp_head):
			print(tmp_head.data)
			tmp_head = tmp_head.next
	def search(self, data):
		tmp_head = self.head
		while (tmp_head):
			if (tmp_head.data == data):
				return tmp_head
			tmp_head = tmp_head.next
	def size(self):
		size = 0
		tmp_head = self.head
		while (tmp_head):
			size += 1
			tmp_head = tmp_head.next
		return size