#Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class linkedList:
    def __init__(self):
        self.head = None
    def insert_Beg(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_end(self, data):
        if self.head is None:
            self.insert_Beg(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    def search_element(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        else:
            return False
    def printt(self):
        itr = self.head
        while itr:
            print(itr.data,end="-->")
            itr = itr.next
        print()
    def searchIndex (self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count += 1
        else:
            return "not found"
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_Beg(data)
        if self.get_length() == index:
            self.insert_end(data)

        itr = self.head
        count = 0
        while itr.next:
            if index - 1 == count:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next


if __name__ == '__main__':
    ll = linkedList()
    ll.insert_Beg(10)
    ll.insert_Beg(20)
    ll.insert_end(35)
    print(ll.search_element(35))
    print(ll.searchIndex(10))
    ll.insert_at_index(3, 12)
    ll.printt()


