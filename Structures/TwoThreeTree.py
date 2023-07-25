import copy


class TwoThreeTree:
    def __init__(self, parent=None):
        """
        +createTwoThreeTree()
        This function creates an empty TwoThreeTree.
        :param parent: This is the parent of the Tree (=None in the beginning, unless given, because root has no parent)
        """
        self.root = []
        self.subtrees = []
        self.parent = parent

    def destroy(self):
        """
        +destroy()
        Destroys a TwoTreeThree.
        """
        del self.parent, self.root, self.subtrees

    def isEmpty(self):
        """
        +isEmpty(): boolean     {query}
        This method returns True when the TwoTreeThree is empty (no elements)
        :return: True --> when the list is empty.
                 False --> when there is at least one element in the list.
        """
        return len(self.root) == 0

    def leaf(self):
        """
        +leaf(): boolean        {query}
        This method checks if a node is a leaf or not.
        :return: True --> when the subtrees are empty (node is leaf).
                 False --> when the subtrees are not empty (node isn't leaf).
        """
        return len(self.subtrees) == 0

    def retrieveItem(self, item):
        """
        +retrieveItem(in self: TwoThreeTree, in item: integer): boolean     {query}
        This method tells if an item is in the TwoThreeTree or not.
        :param item: The item to be retrieved from the TwoThreeTree.
        :return: True if item in TwoThreeTree and False if not retrieved.
        """
        if item in self.root:
            return True
        elif self.leaf():
            return False
        else:
            if item < self.root[0]:
                return self.subtrees[0].retrieveItem(item)
            elif len(self.root) == 1:
                return self.subtrees[1].retrieveItem(item)
            elif len(self.root) == 2:
                if item < self.root[1]:
                    return self.subtrees[1].retrieveItem(item)
                else:
                    return self.subtrees[2].retrieveItem(item)

    def inorder(self, array=None):
        """
        +inorder(in self: TwoThreeTree, in array: vector of integers)     {query}
        This method traverses every item in the tree in the order: first go to the lefttree of the TwoThreeTree.
        If lefttree is fully traversed than go to the root and after the root, go to righttree of the TwoThreeTree.
        :param array: array is an empty list. This list is the list to keep the order of the items in which they are
        traversed. Normally in the order small to large.
        :return: The array "array" (see in param).
        """
        if array is None:
            array = []
        if self.leaf():
            array.extend(self.root)
        else:
            for i in range(len(self.root)):
                array = self.subtrees[i].inorder(array)
                array.append(self.root[i])
            self.subtrees[len(self.root)].inorder(array)
        return array

    def split(self):
        """
        +split(in self: TwoThreeTree)
        This function splits a node when a node has 3 items in the root.
        """
        if self.parent is None:
            old_subtrees = copy.deepcopy(self.subtrees)
            self.subtrees.clear()
            self.subtrees.extend((TwoThreeTree(self), TwoThreeTree(self)))
            self.subtrees[0].root.append(self.root[0])
            self.subtrees[1].root.append(self.root[2])
            self.root = [self.root[1]]
            if old_subtrees != []:
                self.subtrees[0].subtrees.extend((old_subtrees[0], old_subtrees[1]))
                self.subtrees[1].subtrees.extend((old_subtrees[2], old_subtrees[3]))
                self.subtrees[0].subtrees[0].parent = self.subtrees[0].subtrees[1].parent = self.subtrees[0]
                self.subtrees[1].subtrees[0].parent = self.subtrees[1].subtrees[1].parent = self.subtrees[1]
        else:
            self.parent.root.append(self.root[1])
            self.parent.root.sort()
            self.root.pop(1)
            if len(self.parent.root) == 2:
                i = self.parent.subtrees.index(self) + 1
                self.parent.subtrees.insert(i, TwoThreeTree(self.parent))
                self.parent.subtrees[i].root.append(self.root[1])
                if not self.leaf():
                    self.parent.subtrees[i].subtrees.extend((self.subtrees[2], self.subtrees[3]))
                    self.parent.subtrees[i].subtrees[0].parent = self.parent.subtrees[i].subtrees[1].parent = self.parent.subtrees[i]
                    self.subtrees = self.subtrees[0:2]
                self.root.pop(1)
            else:
                i = self.parent.subtrees.index(self)
                self.parent.subtrees.insert(i, TwoThreeTree(self.parent))
                self.parent.subtrees[i].root.append(self.root[0])
                self.root.pop(0)
                if not self.leaf():
                    self.parent.subtrees[i].subtrees.extend((self.subtrees[0], self.subtrees[1]))
                    self.parent.subtrees[i].subtrees[0].parent = self.parent.subtrees[i].subtrees[1].parent = self.parent.subtrees[i]
                    self.subtrees = self.subtrees[2:4]
            if len(self.parent.root) == 3:
                self.parent.split()

    def insert(self, item):
        """
        +insert(in self: TwoThreeTree, in item: integer, out success: boolean)
        Adds new item to a TwoThreeTree with items with different search key values, different from the search key of
        new item. Success indicates whether the addition was successful.
        :param item: The item that's going to be inserted, different from the items that are already in the tree.
        :return: Returns the item that is inserted and success = True if item is successfully inserted. Success = False
        if item is not successfully inserted.
        """
        if self.leaf():
            self.root.append(item)
            self.root.sort()
            if len(self.root) == 3:
                self.split()
        else:
            if item < self.root[0]:
                self.subtrees[0].insert(item)
            elif len(self.root) == 1:
                self.subtrees[1].insert(item)
            elif len(self.root) == 2:
                if item < self.root[1]:
                    self.subtrees[1].insert(item)
                else:
                    self.subtrees[2].insert(item)
        return item, True

    def inordersuccesor(self, item):
        """
        +inordersuccesor(in self: TwoThreeTree, in item: integer, out insuc: TwoTreeThree)
        Finds the inorder succesor of a node.
        :param item: The item whose inorder successor must be found.
        :return: Returns a TwoTreeThree, this is Three where the inorder succesor is on index 0.
        """
        if self.leaf():
            return self
        insuc = self.subtrees[self.root.index(item) + 1]
        while insuc.subtrees:
            insuc = insuc.subtrees[0]
        return insuc

    def redistribute(self):
        """
        +redistribute(in self: TwoThreeTree)
        This function redistributes the item on a path for deleting aan item.
        """
        if len(self.parent.root) == 1:
            if self.parent.subtrees.index(self) == 0:
                self.parent.subtrees[0].root.append(self.parent.root[0])
                self.parent.root[0] = self.parent.subtrees[1].root[0]
                self.parent.subtrees[1].root.pop(0)
                if self.parent.subtrees[1].subtrees != []:
                    self.parent.subtrees[1].subtrees[0].parent = self.parent.subtrees[0]
                    self.parent.subtrees[0].subtrees.append(self.parent.subtrees[1].subtrees[0])
                    self.parent.subtrees[1].subtrees.pop(0)
            else:
                self.parent.subtrees[1].root.append(self.parent.root[0])
                self.parent.root[0] = self.parent.subtrees[0].root[-1]
                self.parent.subtrees[0].root.pop()
                if self.parent.subtrees[0].subtrees != []:
                    self.parent.subtrees[0].subtrees[-1].parent = self.parent.subtrees[1]
                    self.parent.subtrees[1].subtrees.insert(0, self.parent.subtrees[0].subtrees[-1])
                    self.parent.subtrees[0].subtrees.pop()
        else:
            if self.parent.subtrees.index(self) == 0:
                self.parent.subtrees[0].root.append(self.parent.root[0])
                self.parent.root[0] = self.parent.subtrees[1].root[0]
                self.parent.subtrees[1].root.pop(0)
                if self.parent.subtrees[1].subtrees != []:
                    self.parent.subtrees[1].subtrees[0].parent = self.parent.subtrees[0]
                    self.parent.subtrees[0].subtrees.append(self.parent.subtrees[1].subtrees[0])
                    self.parent.subtrees[1].subtrees.pop(0)
            elif self.parent.subtrees.index(self) == 1:
                if len(self.parent.subtrees[0].root) == 2:
                    self.parent.subtrees[1].root.append(self.parent.root[0])
                    self.parent.root[0] = self.parent.subtrees[0].root[1]
                    self.parent.subtrees[0].root.pop()
                    if self.parent.subtrees[1].subtrees != []:
                        self.parent.subtrees[0].subtrees[2].parent = self.parent.subtrees[1]
                        self.parent.subtrees[1].subtrees.insert(0, self.parent.subtrees[0].subtrees[2])
                        self.parent.subtrees[0].subtrees.pop()
                else:
                    self.parent.subtrees[1].root.append(self.parent.root[1])
                    self.parent.root[1] = self.parent.subtrees[2].root[0]
                    self.parent.subtrees[2].root.pop(0)
                    if self.parent.subtrees[1].subtrees != []:
                        self.parent.subtrees[2].subtrees[0].parent = self.parent.subtrees[1]
                        self.parent.subtrees[1].subtrees.append(self.parent.subtrees[2].subtrees[0])
                        self.parent.subtrees[2].subtrees.pop(0)
            else:
                self.parent.subtrees[2].root.append(self.parent.root[1])
                self.parent.root[1] = self.parent.subtrees[1].root[1]
                self.parent.subtrees[1].root.pop()
                if self.parent.subtrees[1].subtrees != []:
                    self.parent.subtrees[1].subtrees[2].parent = self.parent.subtrees[2]
                    self.parent.subtrees[2].subtrees.insert(0, self.parent.subtrees[1].subtrees[2])
                    self.parent.subtrees[1].subtrees.pop()

    def merge(self):
        """
        +merge(in self: TwoThreeTree)
        This function merges nodes together when necessary.
        """
        if len(self.parent.root) == 1:
            if self.parent.subtrees.index(self) == 0:
                if self.parent.subtrees[0].subtrees != []:
                    only_subtree = self.parent.subtrees[0].subtrees[0]
                    self.parent.subtrees[1].subtrees.insert(0, only_subtree)
                    only_subtree.parent = self.parent.subtrees[1]
                self.parent.subtrees.pop(0)
            else:
                if self.parent.subtrees[1].subtrees != []:
                    only_subtree = self.parent.subtrees[1].subtrees[0]
                    self.parent.subtrees[0].subtrees.append(only_subtree)
                    only_subtree.parent = self.parent.subtrees[0]
                self.parent.subtrees.pop(1)
            self.parent.subtrees[0].root.append(self.parent.root[0])
            self.parent.subtrees[0].root.sort()
            self.parent.root.pop(0)
        else:
            if self.parent.subtrees.index(self) == 0:
                if self.parent.subtrees[0].subtrees != []:
                    only_subtree = self.parent.subtrees[0].subtrees[0]
                    self.parent.subtrees[1].subtrees.insert(0, only_subtree)
                    only_subtree.parent = self.parent.subtrees[1]
                self.parent.subtrees.pop(0)
                self.parent.subtrees[0].root.append(self.parent.root[0])
                self.parent.subtrees[0].root.sort()
                self.parent.root.pop(0)
            elif self.parent.subtrees.index(self) == 1:
                if self.parent.subtrees[1].subtrees != []:
                    only_subtree = self.parent.subtrees[1].subtrees[0]
                    self.parent.subtrees[0].subtrees.append(only_subtree)
                    only_subtree.parent = self.parent.subtrees[0]
                self.parent.subtrees.pop(1)
                self.parent.subtrees[0].root.append(self.parent.root[0])
                self.parent.subtrees[0].root.sort()
                self.parent.root.pop(0)
            else:
                if self.parent.subtrees[2].subtrees != []:
                    only_subtree = self.parent.subtrees[2].subtrees[0]
                    self.parent.subtrees[1].subtrees.append(only_subtree)
                    only_subtree.parent = self.parent.subtrees[1]
                self.parent.subtrees.pop()
                self.parent.subtrees[1].root.append(self.parent.root[1])
                self.parent.subtrees[1].root.sort()
                self.parent.root.pop(1)

    def fix(self):
        """
        +fix(in self: TwoThreeTree)
        The removal is completed by the fix by removing the root, the redistribute items from joining nodes.
        """
        if self.parent is None:
            new_tree = TwoThreeTree()
            if self.subtrees != []:
                new_tree = self.subtrees[0]
            self.subtrees.clear()
            self.root = new_tree.root
            self.subtrees = new_tree.subtrees
            if self.subtrees != []:
                self.subtrees[0].parent = self.subtrees[1].parent = self.subtrees[2].parent = self
        else:
            if self.parent.subtrees.index(self) == 0 or self.parent.subtrees.index(self) == 2:
                if len(self.parent.subtrees[1].root) == 2:
                    self.redistribute()
                else:
                    self.merge()
                    if self.parent.root == []:
                        self.parent.fix()
            elif self.parent.subtrees.index(self) == 1:
                if len(self.parent.root) == 2:
                    if len(self.parent.subtrees[0].root) == 2:
                        self.redistribute()
                    else:
                        if len(self.parent.subtrees[2].root) == 2:
                            self.redistribute()
                        else:
                            self.merge()
                        if self.parent.root == []:
                            self.parent.fix()
                else:
                    if len(self.parent.subtrees[0].root) == 2:
                        self.redistribute()
                    else:
                        self.merge()
                        if self.parent.root == []:
                            self.parent.fix()

    def delete(self, item):
        """
        +delete(in self: TwoThreeTree, in item: integer, out succes: boolean)
        :param item: This is the item that is going to be deleted in the TwoThreeTree.
        :return: Returns the item that is deleted and a boolean: True if item is deleted
                                                                 False if item is not deleted
        """
        if self.leaf() and item not in self.root:
            return item, False
        if item in self.root:
            inordersuc = self.inordersuccesor(item)
            self.root[self.root.index(item)] = inordersuc.root[0]
            inordersuc.root.pop(0)
            if inordersuc.root == []:
                inordersuc.fix()
            return item, True
        else:
            if item < self.root[0]:
                return self.subtrees[0].delete(item)
            elif len(self.root) == 1:
                return self.subtrees[1].delete(item)
            elif len(self.root) == 2:
                if item < self.root[1]:
                    return self.subtrees[1].delete(item)
                else:
                    return self.subtrees[2].delete(item)

    def toDot(self, name):
        """
        +toDot(in name: string)    {query}
        This function writes a .dot file with a given name for the TwoThreeTree.
        """
        file = open(str(name) + ".dot", "w+")
        file.write("Graph{\n")
        self.content(file)
        file.write("}")

    def content(self, file):
        """
        +content(in file: .dot-file)    {query}
        This function is an auxiliary function for the function "toDot". This function writes the content
        of the .dot file.
        """
        for i in self.subtrees:
            file.write("\"")
            if len(self.root) == 1:
                file.writelines(str(self.root[0]))
            elif len(self.root) == 2:
                file.writelines(str(self.root[0]) + " | " + str(self.root[1]))
            file.write("\"--\"")
            if len(i.root) == 1:
                file.writelines(str(i.root[0]))
            elif len(i.root) == 2:
                file.writelines(str(i.root[0]) + " | " + str(i.root[1]))
            file.write("\" \n")
            i.content(file)