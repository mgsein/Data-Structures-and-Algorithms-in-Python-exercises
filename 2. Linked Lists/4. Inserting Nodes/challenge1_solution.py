class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None 

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        if self.head.data > data:
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.next.data == current.data:
                current.next = current.next.next
            else:
                current = current.next

    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next 
        print('->'.join(output))

elements = [2,2,3,3,3,4,5]

ll = LL()
for e in elements:
    ll.insert(e)
ll.print()

ll.remove_duplicates()
ll.print()
