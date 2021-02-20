#Write a Python program to find the size of a singly linked list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class linkedList:
    def __init__(self):
        self.head = None
    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_end(self, data):
        if self.head is None:
            self.insert_beg(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    def list_size(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
if __name__ == '__main__':
    ll = linkedList()
    ll.insert_beg(20)
    ll.insert_beg(20)
    ll.insert_end(50)
    print(ll.list_size())
