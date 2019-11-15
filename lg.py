class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.start = None

    def insert_at_end(self, data):
        if self.start is None:
            new_node = Node(data)
            self.start = new_node
            return
        n = self.start
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def delete_start(self):
        if self.start is None:
            print("list has no element to delete")
            return
        if self.start.next is None:
            self.start = None
            return
        self.head = self.start.next
        self.tail = None

    def print(self):
        if self.start is None:
            print("list is empty")
            return
        else:
            n = self.start
            while n is not None:
                print(n.item, " ")
                n = n.next


class LRU:
    def __init__(self, max_cap):
        self.LRU = {}
        self.max_cap = max_cap
        self.list = DoublyLinkedList()
        self.size = 0

    def get(self, key):
        if key not in self.LRU:
            return -1
        node = self.LRU[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        DoublyLinkedList.insert_at_end(node)
        return node.item

    def put(self, key, value):
        if key in self.value:
            DoublyLinkedList.delete_start(self.value[key])
        new_node = Node(key, value)
        self.item[key] = new_node

        if len(self.value) > self.max_cap:
            DoublyLinkedList.delete_start(self.head.next)
        DoublyLinkedList.insert_at_end(new_node)
        return

    def size(self):
        return self.size

    def max_capacity(self):
        return self.max_cap
