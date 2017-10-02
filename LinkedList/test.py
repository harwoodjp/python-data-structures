from impl import LinkedList

linked_list = LinkedList()
linked_list.insert("bob")
linked_list.insert("tim")
linked_list.insert("sally")
linked_list.insert("roger")
linked_list.insert("shelly")
#linked_list.print()
print(linked_list.search("shelly").data)