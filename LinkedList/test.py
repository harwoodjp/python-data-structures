import pytest
from impl import Node, LinkedList

@pytest.mark.parametrize("data_list", [[1,2,3,4]])
def test_insert(data_list):
	linkedList = LinkedList()
	
	for data in data_list:
		print("data")
		linkedList.insert(data)

	tmp_head = linkedList.head
	for data in list(reversed(data_list)):
		assert(data == tmp_head.data)
		tmp_head = tmp_head.next