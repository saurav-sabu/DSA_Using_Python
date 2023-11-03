
class Node:

    def __init__(self, item=None, next=None):
        self.item = item  # The data stored in the node
        self.next = next  # Reference to the next node


class SLL:

    def __init__(self, start=None):
        self.start = start  # The starting node of the linked list

    def is_empty(self):

        if self.start is None:
            return True
        else:
            return False

    def insert_at_start(self, data):
        # Insert a new node with data at the beginning of the linked list
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        # Insert a new node with data at the end of the linked list
        n = Node(data)

        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def search(self, data):
        # Search for a node with the given data and return it
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

        return None

    def insert_after(self, data, temp):
        # Insert a new node with data after the specified node
        n = Node(data, temp.next)

        if temp is not None:
            temp.next = n

    def print_list(self):
        # Print the linked list
        temp = self.start

        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next

        print()

    def delete_first(self):
        # Delete the first node in the linked list
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next

    def delete_last(self):
        # Delete the last node in the linked list
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:  # previous node
                temp = temp.next
            temp.next = None

    def delete_item(self, data):
        # Delete the node with the specified data
        if self.is_empty():
            pass
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        # Create an iterator for the linked list
        return SLLIterator(self.start)


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        # Iterate through the linked list using the iterator
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# driver code
obj = SLL()

obj.insert_at_start(20)
obj.print_list()
obj.insert_at_start(10)
obj.insert_at_last(30)
obj.insert_at_last(100)
obj.insert_at_start(50)
obj.print_list()
obj.insert_after(45, obj.search(30))
obj.print_list()
obj.delete_first()
obj.print_list()
obj.delete_last()
obj.print_list()
obj.delete_item(30)
obj.print_list()
for x in obj:
    print(x, end=" ")
