class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value
        self.count = 1

    def insert(self, value):
        if self.value == value:
            self.count += 1
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(str(self.value) + " : " + str(self.count))
        if self.right is not None:
            self.right.print_tree()

    def count_words(self):
        if self.left and self.right:
            return self.count + self.left.count_words() + self.right.count_words()
        elif self.left:
            return self.count + self.left.count_words()
        elif self.right:
            return self.count + self.right.count_words()
        else:
            return self.count

    def write_tree(self, file_w):
        if self.left is not None:
            self.left.write_tree(file_w)
        file_w.write(str(self.value) + " : " + str(self.count) + '\n')
        if self.right is not None:
            self.right.write_tree(file_w)

    def export_tree(self, filename):
        with open(filename, 'w', encoding='utf-8') as file_w:
            self.write_tree(file_w)


def search(tree, key):
    while True:
        try:
            if tree.value.startswith(key):
                print(tree.value, ':', tree.count)
                return
            elif key < tree.value:
                tree = tree.left
            elif key > tree.value:
                tree = tree.right
        except AttributeError:
            print('слово ' + key + ' не найдено')
            return
