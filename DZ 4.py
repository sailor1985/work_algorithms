from typing import Any
import enum

class Color(enum.Enum):
    RED = True
    BLACK = False

class Node:
    #Красно-черные узлы дерева, цвет узла по умолчанию - красный
    def __init__(self, value: Any):
        self.val: Any = value
        self.color: Color = Color.RED
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node(val={self.val}, color={self.color.value}, left={self.left}, right={self.right})'

class RBT:
    def __init__(self):
        self.root = None

    def insert(self, value: Any) -> None:
        #Вставка и обновление корневого каталога
        self.root = self.__insert(self.root, value)
        self.root.color = Color.BLACK

    def __insert(self, root: Node, val: Any) -> Node:
        #Рекурсивная вставка
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = self.__insert(root.left, val)
        elif val > root.val:
            root.right = self.__insert(root.right, val)
        else:
            root.val = val

        if self.is_red(root.right) and not self.is_red(root.left):
            root = self.rotate_left(root)
        if self.is_red(root.left) and self.is_red(root.left.left):
            root = self.rotate_right(root)
        if self.is_red(root.left) and self.is_red(root.right):
            self.flip_color(root)

        return root

    @staticmethod
    def is_red(node: Node) -> bool:
        """Функция проверки, если узел красный.
           Пустые узлы считаются ЧЕРНЫМИ
           Возвращает: Boolean value в зависимости от того, красный ли узел
        """
        if node is None:
            return False
        return node.color == Color.RED

    @staticmethod
    def flip_color(node: Node) -> None:
        """ Меняет цвет, если оба ребенка (левый и правый) красные"""
        node.color = Color.RED
        node.left.color = Color.BLACK
        node.right.color = Color.BLACK

    def rotate_left(self, node: Node) -> Node:
        """Поворот влево нового узла, если правый узел красный
        Аргументы:
            узел: Узел, который имеет красный узел справа
        Возвращает: повернутый новый узел
        """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        new_root.color = node.color
        node.color = Color.RED
        print("Left Rotation !!")
        return new_root

    def rotate_right(self, node: Node) -> Node:
        """Поворот вправо нового узла,если левый и левый левый узел красные
        Аргументы:
            узел: Узел, у которого оба ребенка (левый и левый левый) красные
        Возвращает: повернутый новый узел
        """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        new_root.color = node.color
        node.color = Color.RED
        print("Right Rotation !!")
        return new_root

    def inorder(self) -> None:
        """Обход по порядку для root"""
        self.__inorder(self.root)

    def __inorder(self, root: Node) -> None:
        """Рекурсивный обход по порядку для любого узла"""
        if root is None:
            return
        self.__inorder(root.left)
        print(root.val, end=" ")
        self.__inorder(root.right)


if __name__ == "__main__":
    '''
            root
            |
            40
        // \
        20 50
        / \
        10 30
            //
        25
    '''

    rbt = RBT()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(40)
    rbt.insert(50)
    rbt.insert(25)
    rbt.inorder()
