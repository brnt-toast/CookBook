class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key: 
                self.head = temp.next
                temp = None
                return 

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return 

        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False


    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = SinglyLinkedList()
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)

print("Linked list after inserts:")
linked_list.traverse()

print("Searching for 2 in Linked List:", linked_list.search(2))

linked_list.delete_node(2)
print("Linked list after deleting 2:")
linked_list.traverse()

print("Searching for 2 in Linked List:", linked_list.search(2))
