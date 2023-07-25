import copy


class Heap:
    def __init__(self):
        """
        +createHeap()
        This function creates an empty Heap.
        """
        self.array = [None] * 255

    def destroyHeap(self):
        """
        +destroyHeap()
        This function destroys a Heap.
        """
        del self.array

    def heapisEmpty(self):
        """
        +isEmpty(): boolean {query}
        :return: Returns the boolean True if heap is empty and False if the heap is not empty.
        """
        return self.array[0] is None

    def heapRetrieve(self, newItem):
        """
        +retrieve(in value: integer, out newItem: integer, out success: boolean)
        :param newItem: The item that is going to be retrieved.
        :return: Returns the item to retrieve and a boolean: True if the item is retrieved in the Binary Tree.
                                                             False if the item is not retrieved in the Binary Tree.
        """
        i = 0
        while self.array[i] is not None:
            if self.array[i] == newItem:
                return newItem, True
            i += 1
        return newItem, False

    def heapInsert(self, newItem):
        """
        +heapInsert(in newItem: integer, out newItem: integer, out success: boolean)
        Adds new item to the heap with items with different
        search key values, different from the search key of new item.
        Success indicates whether the addition was successful.
        :param newItem: The item that's going to be inserted, different from the items that are already in the tree.
        :return: Returns True if item is succesfully inserted else returns False if item is not succesfully inserted.
        """
        if self.heapRetrieve(newItem)[1]:
            return newItem, False
        i = self.array.index(None)
        self.array[i] = newItem
        self.TrickleUp(i)
        return newItem, True

    def heapDelete(self):
        """
        +heapDelete(out rootItem: integer, out succes boolean)
        Puts the item in the root in the rootItem en deletes it after out of the heap.
        This item has the biggest search Key value.
        :return: Success is false when the heap is empty else success is true.
        """
        if self.heapisEmpty():
            return False
        rootitem = self.array[0]
        i = self.array.index(None) - 1
        self.array[0] = self.array[i]
        self.array[i] = None
        self.TrickleDown(0)
        return rootitem, True

    def TrickleUp(self, index):
        """
        +TrickleUp(in index: integer)
        This function sets the item in the right position by index
        :param index: This is the item that has to be put in the right place of the heap
        """
        if index != 0:
            if self.array[int((index - 1)/2)] < self.array[index]:
                temp_value = self.array[int((index - 1) / 2)]
                self.array[int((index - 1) / 2)] = self.array[index]
                self.array[index] = temp_value
            self.TrickleUp(int((index - 1) / 2))

    def replace(self, index, childnode):
        temp_value = self.array[index]
        self.array[index] = self.array[(index * 2) + childnode]
        self.array[(index * 2) + childnode] = temp_value
        self.TrickleDown((index * 2) + childnode)

    def TrickleDown(self, index):
        """
        +TrickleDown(in index: integer)
        This function sets the item in the right position by index
        :param index: This is the item that has to be put in the right place of the heap
        """
        if self.array[(index * 2) + 1] is not None and self.array[(index * 2) + 2] is not None:
            if self.array[(index * 2) + 2] > self.array[(index * 2) + 1] and self.array[(index * 2) + 2] > self.array[index]:
                self.replace(index, 2)
            elif self.array[(index * 2) + 1] > self.array[(index * 2) + 2] and self.array[(index * 2) + 1] > self.array[index]:
                self.replace(index, 1)
        elif self.array[(index * 2) + 1] is not None and self.array[(index * 2) + 1] > self.array[index]:
            self.replace(index, 1)

    def Printsorted(self):
        temp_heap = copy.deepcopy(self)
        sortedarray = []
        while temp_heap.array[0] is not None:
            i = temp_heap.array.index(None) - 1
            sortedarray.insert(0, temp_heap.array[0])
            temp_heap.array[0] = temp_heap.array[i]
            temp_heap.array[i] = None
            temp_heap.TrickleDown(0)
        return sortedarray

    def toDot(self, name):
        """
        +toDot(in name: string)
        This function writes a .dot file with for the Heap.
        :param name: This is a string, this is also the name given to the .dot file.
        """
        bestandnaam = name + ".dot"
        file = open(bestandnaam, "w+")
        file.write("Graph G {\n")
        i = 0
        while self.array[i] is not None:
            file.write("node[style=circle]" + str(self.array[i]) + "\n")
            i += 1
        i = 0
        while self.array[i] is not None:
            if self.array[(i * 2) + 1] is not None:
                file.write(str(self.array[i]) + "--" + str(self.array[(i * 2) + 1]) + "\n")
            else:
                file.write('"' + "a+" + str(i) + '"' + "[style=invis]\n")
                file.write(str(self.array[i]) + "--" + '"' + "a+" + str(i) + '"' + "[style=invis]\n")
            if self.array[(i * 2) + 2] is not None:
                file.write(str(self.array[i]) + "--" + str(self.array[(i * 2) + 2]) + "\n")
            else:
                file.write('"' + "a+" + str(i) + '"' + "[style=invis]\n")
                file.write(str(self.array[i]) + "--" + '"' + "a+" + str(i) + '"' + "[style=invis]\n")
            i += 1
        file.write("}")
