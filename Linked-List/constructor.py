# We create a class for Node because we dont
# always want to write code that creeates a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # Creates a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4)

print(my_linked_list.head.value)
# def append(self, value):
# # Creates new node and adds note to end
# def prepend(self, value):
# # Creates new node and adds note to beginning
# def insert(self, index, value):
# # Creates new node and inserts node
