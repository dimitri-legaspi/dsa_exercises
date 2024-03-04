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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # This function is to return the LL after we pop the tail
    def pop(self):
        # Edge case for an empty list
        if self.length == 0:
            return None
        # We set temp and pre to head so that we can keep
        # track of the node
        temp = self.head
        pre = self.head
        # Iterates trhough the LL, we check to see if temp.next is pointing
        # at another node
        while (temp.next is not None):
            # In the iterations the pre  will always point
            # at the current node, and temp will be at the next node
            pre = temp
            temp = temp.next
        # When we get to the last node, self.tail is = to pre
        # then we set the tail pointer to None
        # Then we decrease the length by 1
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # This if statement is after we decrease the LL to 0
        # This edge case checks to correct
        # head and tail if it points to no node so we set
        # head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None
        # This returns the value of the removed node
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - returns 2 Node
print(my_linked_list.pop())
# (1) Item - returns 1 Node
print(my_linked_list.pop())
# (0) Item - returns None
print(my_linked_list.pop())
