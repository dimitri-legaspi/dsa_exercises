class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #  Add a node to the end of the linked list
    def append(self, value):
        # Creates a new node
        new_node = Node(value)
        # First we have to determine if the list is empty
        # If it is then the head and tail point to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # Seting the pointer to point to the new node
        # Setting the tail to the new node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(11)

my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()
