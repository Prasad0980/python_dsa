class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        # new_node = Node(value)
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1
        self.head = self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        val = list()
        while temp:
            val.append(temp.value)
            temp = temp.next
        return '->'.join([str(item) for item in val])

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insert(self, pos, value):
        if pos == 1 or pos == 0:
            self.prepend(value)
        elif pos == self.length or pos > self.length:
            self.append(value)
        else:
            temp = self.head
            count = 1
            while count < pos-1:
                temp = temp.next
                count += 1
            node = Node(value)
            node.next = temp.next
            temp.next = node
            self.length += 1

    def traversal(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
            
    def search(self,target):
        cur = self.head 
        while cur:
            if cur.value == target:
                return True 
            cur = cur.next
        return False 
    
    def pop(self, index):#index starts from 1
        temp = self.head
        for _ in range(index-1):
            temp = temp.next 
        if temp == self.head:
            self.head = self.head.next
            temp.next = None 
            return temp 

l1 = LinkedList()
l1.insert(1, 1)
l1.insert(4, 1)
l1.insert(3, 1)
l1.insert(2, 5)
l1.insert(3, 6)
l1.insert(1, 0)
print(l1)
print(l1.search(11))