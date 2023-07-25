class BinarySearchTree:
    def __init__(self, parent=None, root=None, leftTree=None, rightTree=None):
        """
        +createBinaryTree()
        This function creates an empty Binary Tree.
        :param parent: This is the parent of the Tree (=None in the beginning because root has no parent)
        :param root: This is the root of the Tree
        :param leftTree: This is the leftsubtree
        :param rightTree: This is the rightsubtree
        """
        self.parent = parent
        self.leftTree = leftTree
        self.rightTree = rightTree
        self.root = root

    def destroy(self):
        """
        +destroyBinaryTree(in self: BinaryTree)
        This function deletes a Binary Tree.
        """
        del self.leftTree
        del self.parent
        del self.rightTree
        del self.root

    def insert(self, item):                                             # this function inserts an item in the tree
        """
        +insert(in self: BinaryTree, in item: integer, out success: boolean)
        Adds new item to a binary search tree with items with different
        search key values, different from the search key of new item.
        Success indicates whether the addition was successful.
        :param item: The item that's going to be inserted, different from the items that are already in the tree.
        :return: Returns the item that is inserted and success = True if item is succesfully inserted. Success = False
        if item is not succesfully inserted.
        """
        if self.root is None:
            self.root = item
            return item, True
        else:                                                           # if root is not None
            if self.retrieve(item):
                return item, False
            else:
                if item < self.root and self.leftTree is None:              # check where the item needs to be placed
                    self.leftTree = BinarySearchTree(self, item)
                elif item < self.root and self.leftTree is not None:        # if lefttree already exists
                    self.leftTree.insert(item)                              # do an insert in lefttree
                elif item > self.root and self.rightTree is None:
                    self.rightTree = BinarySearchTree(self, item)
                elif item > self.root and self.rightTree is not None:       # if righttree already exists
                    self.rightTree.insert(item)                             # do an insert in righttree
                return item, True

    def isEmpty(self):
        """
        +isEmpty(in self: BinaryTree): boolean {query}
        :return: Returns a boolean: True if tree is empty
                                    False if tree is not empty
        """
        return self.root is None

    def retrieve(self, searchKey):
        """
        +searchTreeRetrieve(in self: BinaryTree, in searchKey: integer, out success: boolean)
        :param searchKey: The item that is going to be retrieved.
        :return: A boolean: True if the item is retrieved in the Binary Tree.
                            False if the item is not retrieved in the Binary Tree.
        """
        if self.isEmpty():
            return False
        elif self.root == searchKey:
            return True
        elif searchKey < self.root and self.leftTree is None:
            return False
        elif searchKey < self.root and self.leftTree is not None:
            return self.leftTree.retrieve(searchKey)
        elif searchKey > self.root and self.rightTree is None:
            return False
        elif searchKey > self.root and self.rightTree is not None:
            return self.rightTree.retrieve(searchKey)

    def inorderTraversal(self, lijst=[]):                                         # this function
        """
        +inorderTraversal(in self: BinaryTree, in lijst: vector of integers)
        This function traverses every item in the tree in the order: first go to the lefttree of the Binary Tree. If
        lefttree fully traversed than go to the root and after the root, go to the righttree of the Binary Tree.
        :param lijst: lijst is an empty list. This list is the list to keep the order of the items in
        which they are travesed
        :return: The list "lijst" (see in param)
        """
        if self.root is None:
            return
        if self.leftTree is not None:
            self.leftTree.inorderTraversal()
        lijst.append(self.root)
        if self.rightTree is not None:
            self.rightTree.inorderTraversal()
        return lijst

    def preorderTraversal(self, lijst=None):                                         # this function
        """
        +preorderTraversal(in self: BinaryTree, in lijst: vector of integers)
        This function traverses every item in the tree in the order: first go to the root of the Binary Tree. Then
        go to the lefttree and after the lefttree is fully traversed, go to the righttree of the Binary Tree.
        :param lijst: lijst is an empty list. This list is the list to keep the order of the items in
        which they are travesed
        :return: The list "lijst" (see in param)
        """
        if lijst is None:
            lijst = []
        if self.root is None:
            return
        lijst.append(self.root)
        if self.leftTree is not None:
            self.leftTree.preorderTraversal()
        if self.rightTree is not None:
            self.rightTree.preorderTraversal()
        return lijst

    def inordersuccesor(self):              # This function keeps goign left until ther eis no lefttree.
        """
        +inordersuccesor(in self: BinaryTree, out inordersuccesor: integer)
        Finds the inorder succesor of a node.
        :return: Returns an integer, this is the inorder succesor
        """
        if self.leftTree is None:
            return self
        else:
            return self.leftTree.inordersuccesor()

    def delete(self, item):
        """
        +delete(in item: integer, out item, integer, out success: boolean)
        This function deletes an item in a Binary Tree and returns the item and a boolean.
        :param item: This is the item that is going to be deleted in the Binary Tree.
        :return: Returns the item that is deleted and a boolean: True if item is deleted
                                                                 False if item is not deleted
        """
        if not self.retrieve(item):
            return item, False

        elif item == self.root:
            if self.leftTree is not None and self.rightTree is not None:
                temp1 = self.rightTree.inordersuccesor()
                self.root = temp1.root
                if temp1.rightTree is not None:
                    temp1.root = temp1.rightTree.root
                    temp1.leftTree = temp1.rightTree.leftTree
                    temp1.rightTree = temp1.rightTree.rightTree
                else:
                    temp1.root = None
                return item, True

            elif self.leftTree is not None:
                lefttree = self.leftTree.leftTree
                righttree = self.leftTree.rightTree
                self.root = self.leftTree.root
                self.leftTree = lefttree
                self.rightTree = righttree
                return item, True

            elif self.rightTree is not None:
                lefttree = self.rightTree.leftTree
                righttree = self.rightTree.rightTree
                self.root = self.rightTree.root
                self.leftTree = lefttree
                self.rightTree = righttree
                return item, True

            else:
                self.root = None
                return item, True
        else:
            if item < self.root:
                return self.leftTree.delete(item)
            elif item > self.root:
                return self.rightTree.delete(item)

    def content(self, file, counter=0):
        """
        +content(in file: textfile, in counter: integer)
        This function is an auxiliary function for the toDot-fucntion. This function writes the contents for the
        Tree.
        :param file: The file that's going to be written.
        :param counter: A counter which holds the number of invisible nodes.
        :return: Returns the counter
        """
        if self.root is None:
            return counter
        if self.root is not None and self.leftTree is not None:
            if self.leftTree.root is None:
                counter += 1
                file.write("a" + str(counter) + "[style=invis]\n")
                file.write(str(self.root) + "--a" + str(counter) + "[style=invis]\n")
            else:
                file.write(str(self.root) + "--" + str(self.leftTree.root) + "\n")
            counter = self.leftTree.content(file, counter)
        else:
            counter += 1
            file.write("a" + str(counter) + "[style=invis]\n")
            file.write(str(self.root) + "--a" + str(counter) + "[style=invis]\n")

        if self.root is not None and self.rightTree is not None:
            file.write(str(self.root) + "--" + str(self.rightTree.root) + "\n")
            counter = self.rightTree.content(file, counter)
        else:
            counter += 1
            file.write("a" + str(counter) + "[style=invis]\n")
            file.write(str(self.root) + "--a" + str(counter) + "[style=invis]\n")
        return counter

    def toDot(self, name):
        """
        +toDot(in name: string)
        This function writes a .dot file with the Binary Tree.
        :param name: This is a string, this is also the name given to the .dot file.
        """
        file = open(str(name) + ".dot", "w+")
        file.write("Graph G {" + "\n")
        self.content(file)
        file.write("}")
