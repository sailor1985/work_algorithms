class Node:
    # Конструктор для создания нового узла
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    # Конструктор для пустого двухсвязного списка
    def __init__(self):
        self.start_node = None

    # Функция разворота двухсвязного списка
    def reverse(self):
        temp = None
        current = self.start_node

        # Меняем местами next и prev для всех узлов двусвязного списка
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Проверка наличия случаев, когда пустой список или список только с одним узлоv
        if temp is not None:
            self.start_node = temp.prev

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

l1 = DoublyLinkedList()
l1.insert_start(2)
l1.insert_start(4)
l1.insert_start(8)
l1.insert_start(10)
l1.print_l()
l1.reverse()
l1.print_l()
