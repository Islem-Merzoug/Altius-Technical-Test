class SinglyLinkedListNode:
    """ Linked list node Structure """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """ Linked list Structure """

    def __init__(self, head=None):
        self.head = head

    def add(self, value):
        """ inserts a new node at the end of this linked list"""
        node = SinglyLinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next

    def logout_linked_list(self):
        """ prints out this linked list for visualization """
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, '->')
            currentNode = currentNode.next
        print('None')

    def compare_lists(self, llistb):
        """ compare between this list and the llistb """
        head1 = self.head
        head2 = llistb.head
        while head1 and head2:
            if head1.value != head2.value:
                return 0

            # let's move to the next nodes
            head1 = head1.next
            head2 = head2.next

        # If we reached the end of both lists
        return head1 is None and head2 is None
