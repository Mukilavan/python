class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked:
    def __init__(self):
        self.head = None

    def append_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def append_end(self, data):
        if self.head is None:
            self.append_beg(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def printt(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print()

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_index(self, index, data):
        if index == 0:
            self.append_beg(data)
        if self.get_length() == index:
            self.append_end(data)

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
    a = Linked()
    a.append_beg(10)
    #a.printt()
    a.append_end(60)
    a.printt()
    print(a.get_length())
    a.insert_at_index(1, 30)
    a.printt()