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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # This function pops the first item in the list
    def pop_first(self):
        #  If the list is empty, then return None
        if self.length == 0:
            return None
        # we set temp to the haed of the LL
        temp = self.head
        # move the head over
        self.head = self.head.next
        # remove the head from the LL
        temp.next = None
        #  decrement length by one
        self.length -= 1
        # This if statement applies if we start with one item
        if self.length == 0:
            self.tail = None
        # this returns the item that was removed from the LL
        return temp


my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) returns 2 Node
print(my_linked_list.pop_first())
# (1) returns 1 Node
print(my_linked_list.pop_first())
# (0) returns None
print(my_linked_list.pop_first())
