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

    # This function will print the LL
    def print_list(self):
        # We set temp to the head of the LL
        temp = self.head
        # Thid will make temp = to each node while this
        # loop goes through the LL
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(11)


my_linked_list.print_list()
